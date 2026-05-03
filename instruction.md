# Final Project Guidance
# Social Network Analysis, Spring 2026
# 1 Background
The final project requires each group to build an AI Agent system for social network analysis. Each group member develops one Skill (a functional module), and the group assembles all Skills into a unified Agent. 

What is a Skill? A Skill is a self-contained, modular unit of functionality that performs a specific task in social network analysis. Each Skill takes well-defined inputs, executes a particular function (e.g., retrieving user profiles, detecting communities, predicting links), and produces structured outputs. Skills are designed to be independently testable and reusable. In this project, each group member is responsible for developing one Skill. 

What is an Agent? An Agent is a system that orchestrates multiple Skills to accomplish a complex, high-level task. The Agent defines the overall workflow: it decides which Skills to invoke, in what order, and how to combine their outputs to produce a final result. For example, an Agent for social influence analysis might coordinate a data collection Skill, a network construction Skill, a centrality computation Skill, and a visualization Skill into a coherent pipeline. In this project, each group builds one Agent by integrating all members’ Skills. 




A concrete example: PokerBot in StudyClawHub (see Fig. 1). PokerBot is an AI Agent that plays Texas Hold’em with real-time coaching. It is composed of five Skills, each developed independently: a poker-strategy Skill (GTO knowledge base and equity calculators), a coachbot Skill (real-time coaching personality), a bot-management Skill (AI opponent lifecycle), a poker-server Skill (game engine and state API), and a pokernow-runtime Skill (adapter for an external poker platform). No Skill depends on the internal implementation of another; they communicate only through a shared data layer. The Agent orchestrator decides when to invoke each Skill based on user input (e.g., “start a game” triggers poker-server and bot-management; asking “was that a good call?” triggers poker-strategy and coachbot). Your social network analysis Agent should follow the same pattern. 
Learning Objectives. Through this project, students are expected to: 
1. Learn to use AI-powered development platforms including OpenClaw, Claude Code, and WorkBuddy. 
2. Understand the concepts of Agents and Skills, and apply them to solve real-world social network analysis tasks. 
3. Practice the open-source workflow in the AI era, including collaborative development, code publishing, and technical report writing. 
# 2 StudyClawHub(https://trust-app-ai-lab.github.io/StudyClawHub/)
All Skills and Agents must be published to StudyClawHub, a lightweight skill registry for social network mining powered by GitHub. StudyClawHub allows students to browse, install, and share Skills and Agents with zero server infrastructure. 
## Submission Steps.
1. Submit via tools. Each member submits their individual Skill, and the group submits the Agent that integrates all component Skills. Submission can be done through Claude Code, OpenClaw, or WorkBuddy. 
2. Register on the website. Go to the StudyClawHub website and click “Submit Skill” or “Submit Agent” to fill in the metadata (name, description, version, tags, GitHub repo URL, and author) and complete the registration. 
# 3 Project Requirements and Report Format
Deliverables and Deadline. Each group must submit the following by May 15, 2026. 
Presentations will take place during Week 14. 

1. Group report (Agent): 4 pages, NeurIPS format. 
2. Individual report (Skill): 3 pages per member, NeurIPS format. 
3. Code submission: Agent and all Skills published to StudyClawHub. 
4. Presentation: each group presents their Agent in Week 14. 

Group Formation. Each group consists of at most 5 members. Each member must contribute exactly one Skill to the group Agent. 

Agent Design (Group). The group should design and implement an Agent that performs a meaningful task related to social network analysis. The Agent should: (i) integrate all members’ Skills into a coherent system; (ii) demonstrate a clear workflow where Skills interact or compose to achieve the Agent’s overall goal; (iii) be evaluated on a well-defined task with appropriate metrics. 

Skill Development (Individual). Each member develops one Skill that serves as a functional module within the Agent. A Skill should: (i) have a clearly defined function (e.g., community detection, influence prediction, link prediction, sentiment analysis, information retrieval, or visualization); (ii) be individually testable and produce measurable results; (iii) include references to relevant prior work or methods. 


Table 1: Report specifications. References do not count toward the page limit.

<table><tr><td>Report Type</td><td>Page Limit</td><td>Scope</td></tr><tr><td>Group Report (Agent)</td><td>4 pages</td><td>Overall Agent design, integration, and evaluation</td></tr><tr><td>Individual Report (Skill)</td><td>3 pages</td><td>Individual Skill method, implementation, and results</td></tr></table>
Report Format. Both reports must use the NeurIPS format (this template) and include the following five components. We have published a LatexReport Skill on StudyClawHub that can automatically configure the NeurIPS format for you. 
• Functionality. Clearly describe what the Agent/Skill does, including input/output specifications and how it addresses the target task. 
• References. Cite relevant prior work, methods, or tools that your design builds upon. Discuss how your approach relates to existing literature. 
• Results. Present quantitative or qualitative results with appropriate evaluation metrics. 
• Analysis. Analyze the results: what works, what does not, and why. Ablation studies or error analysis are encouraged. 
• Visualization. Provide at least one meaningful visualization (e.g., network graphs, performance plots, workflow diagrams). 
