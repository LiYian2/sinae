Agent Planner (agent/planner.py)
核心职责: 接收自然语言输入，检测意图，编排三个 Skill 的执行顺序，组合输出。
实现方式:
1. 意图检测 (_detect_intent, 规则式):
   - build_reading_path — 用户说 "I want to learn/enter/study..." 
   - explain_paper — 用户问 "Why is this paper.../Explain..."
   - filter_by_year — 用户说 "Show papers after 2020" + 年份数字
   - find_bridge_papers — 用户问 "bridge/betweenness/connect"
   - visualize — 用户说 "plot/draw/render/visualize"
   - ask_followup — 在已有数据基础上追问（7-day plan, authors, gaps, foundation）
2. 用户画像提取 (_extract_profile, 规则式):
   - 识别用户水平: beginner ("new to"/"introduce") / advanced ("state of the art") / intermediate (默认)
   - 识别时间偏好: last_year / last3_years / last5_years / all
   - 识别期望论文数: 从自然语言中提取数字或根据关键词推断
3. 主题清洗 (_clean_topic, 正则式):
   - 剥离 "I want to learn", "build a reading path for", "I am new to" 等前缀
   - 处理 "I am new to X and want to learn Y" 结构，提取核心主题 Y
   - 剥离 "beginner", "novice" 等身份声明
工作流 (_workflow_build_reading_path):
Step 1: 清洗主题，提取用户画像
Step 2: 调用文献检索 Skill → 获取论文
Step 3: 语料质量检查 (论文太少则扩展检索)
Step 4: 调用图构建 → 调用图分析 Skill
Step 5: 调用阅读路径生成 Skill
Step 6: 自动保存 report.md, graph.png, scores_distribution.png
Step 7: 生成后续追问建议
---
Skill 1: Literature Retrieval (skill_retrieval/retrieval.py)
核心职责: 将自然语言研究目标转化为结构化论文语料库。
实现方式:
1. 查询计划生成 (_generate_query_plan):
   - 基础查询: 原始 topic
   - 精确匹配: "topic"（双引号短语搜索）
   - 水平扩展: 根据 UserLevel 添加后缀（beginner → "survey/tutorial", intermediate → "method/algorithm", advanced → "state-of-the-art"）
   - 前提知识查询: 对 BEGINNER 用户额外生成 broad context queries（如 "attention mechanism", "computer vision survey", "image recognition CNN"）
   - 单词拆分: 如果 topic 有 ≥4 个词，生成前半/后半子查询
   - 总共最多 8 条查询
2. 前提知识映射 (_get_broad_context_terms):
   - 硬编码了常见领域的上下文映射，如:
     - "transformer" → "attention mechanism neural network", "self-attention survey"
     - "vision" → "computer vision deep learning survey", "image recognition convolutional neural network"
     - "graph" → "graph neural network survey"
     - "cfr" → "counterfactual regret minimization"
3. arXiv 检索 (_search_arxiv):
   - 使用 urllib.request 直接调 arXiv API (http://export.arxiv.org/api/query)
   - 解析 XML 响应 (Atom format)，提取 title, authors, year, abstract, id
   - 无 API key 需求
4. OpenAlex 检索 (_search_openalex):
   - 调 https://api.openalex.org/works?search=...
   - 解析 JSON 响应，提取 title, authors, year, citation_count, referenced_works
   - 从 abstract_inverted_index 重建完整摘要文本 (_reconstruct_abstract)
   - 内建 429 重试 + 延迟
   - 无 API key 需求
5. 相关性过滤 (_filter_relevance):
   - 提取 topic 中的有意义关键词（过滤 stopwords: "want", "learn", "study", "beginner", "with", "from" 等 100+ 词）
   - 对于 BEGINNER: 要求 ≥1 个关键词匹配
   - 对于 intermediate/advanced: 要求 ≥2 个关键词匹配
   - 来自 broad queries 的论文豁免过滤（确保前提知识论文保留）
   - 若过滤后 <10 篇则回退保留全部
6. 去重 (_deduplicate):
   - 基于标题 MD5 哈希去重
   - 重复时保留 citation_count 更高的元数据
7. 引用丰富 (_enrich_citations):
   - 对 OpenAlex 来源论文，批量获取 referenced_works
   - 补充 citation_count
8. Demo 模式 (_generate_demo_papers):
   - 生成 20-60 篇合成论文，按年份/类别分类（foundation/method/neural/frontier）
   - 注入真实前提论文 (_inject_prerequisites): 如 Vision Transformer → 注入 "Attention Is All You Need", ResNet, AlexNet
   - 生成引用关系 (_link_demo_citations): 新论文引用老论文，高引用论文被大量引用
输入/输出:
Input:  {topic, max_papers, user_level, time_range}
Output: [Paper(paper_id, title, authors, year, abstract, url, citation_count, references, source)]
---
Skill 2: Research Graph Analysis (skill_graph/)
图构建 (graph_builder.py):
1. 引用边 (_build_citation_edges):
   - 遍历每篇论文的 references 列表
   - 如果被引论文也在语料库中 → 创建 citation 类型边 (weight=1.0)
2. 语义相似度边 (_build_similarity_edges):
   - 提取有摘要的论文（>50 字符）
   - TF-IDF 向量化 (sklearn, max_features=5000, English stopwords)
   - 余弦相似度矩阵
   - 自适应阈值: 超小数据集 (≤5篇) → 0.05; 正常数据集 → 取 70 分位数 × 0.6
   - 当引用边 <5 时阈值降至 0.05，<20 时 0.08
3. 自适应构建 (build):
   - 根据引用边密度自动调整相似度阈值
   - 在引用稀疏时自动增补更多相似度边
图分析 (analysis.py):
1. PageRank (nx.pagerank):
   - 权重边，反映论文在引用网络中的重要性
2. Betweenness Centrality (nx.betweenness_centrality):
   - 权重边，归一化，反映论文连接不同社区的能力
3. Community Detection (nx_community.louvain_communities):
   - Louvain 算法 (seed=42, 确定性)
   - 将论文自动分成研究分支
   - 回退: 若 Louvain 失败则用连通分量
4. 角色评分 (三个自定义评分):
   - foundation_score = 0.4 × age_factor + 0.6 × pagerank
     - 年份越早 + PageRank 越高 → 越可能是奠基性论文
   - bridge_score = 0.5 × betweenness + 0.25 × degree + 0.25 × cross_community
     - Betweenness 高 + 连接多个社区 → 桥梁论文
   - frontier_score = 0.5 × recency + 0.3 × pagerank + 0.2 × community_activity
     - 年份越新 + 所在社区活跃 → 前沿论文
5. 社区信息汇总 (get_community_info):
   - 每个社区的规模、平均年份、Top-3 论文
输入/输出:
Input:  [Paper] (从数据层读取)
Output: {paper_id: NodeScores(pagerank, betweenness, community, foundation_score, bridge_score, frontier_score)}
---
### Skill 3: Reading Path & Report (`skill_reading_path/`)
**阅读路径生成** (`path_generator.py`):
1. **论文分类**:
   - Foundation: `foundation_score` Top-3
   - Core: `pagerank` Top-3
   - Bridge: `bridge_score` Top-2
   - Frontier: `frontier_score` Top-3
   - Prerequisites (仅 BEGINNER): 选出不紧密匹配 topic 但高引用/高影响力的背景论文 (`_select_prerequisites`)
2. **阶段编排** (`_build_stages`):
   - Beginner: Prerequisites → Conceptual Foundations → Core Methods → Bridge → Recent Advances
   - Intermediate: Foundations → Core Algorithms → Bridge → Recent Frontier
   - Advanced: Foundations → Core Methods → Research Gaps → State of the Art
3. **去重**: 使用 `used_ids` 集合确保每篇论文只出现在一个阶段
4. **理由生成** (`_generate_paper_reason`):
   - Foundation 高 PageRank: "Highly cited foundation paper (X citations)"
   - Bridge 高 betweenness: "Key bridge paper connecting multiple research communities"
   - Frontier: "Recent paper (Y) at the research frontier"
   - 通用: 基于分数的描述性理由
**报告生成** (`report.py`):
1. `generate()` — 完整 Briefing Report，含统计、社区、Top 论文
2. `explain_paper_role(paper_id)` — 单篇论文角色分析
3. `generate_bridge_report()` — 桥梁论文报告 (Top-10 by bridge_score)
4. `generate_seven_day_plan()` — 7 天阅读计划 (周一到周日均匀分配)
**可视化** (`visualization.py`):
1. `render_network()` — 论文引用网络图:
   - 节点大小 = PageRank
   - 节点颜色 = 社区归属 (Set3 colormap)
   - 边 = citation + similarity
   - 标注 Top-15 高影响力论文标题
   - Spring layout 布局
   - 只渲染最大连通分量 (>200 节点时调整参数)
2. `render_score_distribution()` — 评分分布直方图 (2×2 subplots)
---
共享数据层 (shared/data_layer.py)
所有 Skill 通过它读写数据，不直接调用对方。存储:
- research_profile — 用户画像
- papers — 论文字典 (paper_id → Paper)
- graph_data — 图结构 (nodes + edges)
- node_scores — 节点评分
- reading_path — 阅读路径
- corpus_quality — 语料质量指标
---
关键指标总结
指标	当前状态
测试覆盖	40/40 pass (4 测试文件)
API 依赖	零 API key (arXiv + OpenAlex 免费)
Demo 模式	合成数据 + 注入真实前提论文 (ResNet, Attention Is All You Need 等)
输出文件	report.md + graph.png + scores_distribution.png
前提知识系统	10+ 领域映射表 + 真实论文注入
意图路由	6 种意图 × 规则式检测
用户水平分层	3 级 (beginner/intermediate/advanced)
