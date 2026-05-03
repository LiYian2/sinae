import sys
import argparse

from agent.planner import AgentPlanner


def main():
    parser = argparse.ArgumentParser(
        description="ResearchTrail: Citation-Network Agent for Personalized Literature Entry and Reading Path Planning",
    )
    parser.add_argument(
        "query",
        nargs="*",
        help="Your research question or command (e.g., 'I want to enter the field of Deep CFR')",
    )
    parser.add_argument(
        "--demo", "-d",
        action="store_true",
        help="Use demo mode with synthetic papers (no API calls)",
    )
    parser.add_argument(
        "--interactive", "-i",
        action="store_true",
        help="Run in interactive mode",
    )
    parser.add_argument(
        "--output", "-o",
        type=str,
        default=None,
        help="Save output to a file",
    )

    args = parser.parse_args()

    agent = AgentPlanner()
    agent.demo = args.demo

    if args.interactive:
        run_interactive(agent, args.output)
    elif args.query:
        query = " ".join(args.query)
        result = agent.process(query)
        print(result)
        if args.output:
            with open(args.output, "w") as f:
                f.write(result)
            print(f"\nOutput saved to {args.output}")
    else:
        parser.print_help()
        print("\nExamples:")
        print("  researchtrail 'I want to enter the field of Deep CFR'")
        print("  researchtrail --demo 'Build a reading path for graph anomaly detection'")
        print("  researchtrail -i")


def run_interactive(agent: AgentPlanner, output_file: str | None):
    mode = "demo" if agent.demo else "live"
    print("=" * 60)
    print(f"  ResearchTrail: Citation-Network Reading Path Agent [{mode}]")
    print("  Type your research goal or follow-up question.")
    print("  Commands: /help, /visualize, /report, /bridge, /exit")
    print("=" * 60)
    print()

    while True:
        try:
            user_input = input("researchtrail> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not user_input:
            continue

        if user_input.startswith("/"):
            cmd = user_input[1:].lower()
            if cmd == "exit" or cmd == "quit":
                print("Goodbye!")
                break
            elif cmd == "help":
                print_help()
                continue
            elif cmd == "visualize":
                user_input = "visualize the network"
            elif cmd == "report":
                user_input = "generate a report"
            elif cmd == "bridge":
                user_input = "find bridge papers"
            elif cmd == "7day":
                user_input = "give me a 7-day reading plan"
            elif cmd == "authors":
                user_input = "which authors should I follow?"
            elif cmd == "foundation":
                user_input = "show foundation papers"
            elif cmd == "gaps":
                user_input = "show research gaps and open problems"

        result = agent.process(user_input)
        print()
        print(result)
        print()

        if output_file:
            with open(output_file, "a") as f:
                f.write(f"\n## Query: {user_input}\n\n{result}\n")


def print_help():
    print("""
Available commands:
  /help        Show this help
  /visualize   Render and save network visualization
  /report      Generate full briefing report
  /bridge      Find bridge papers between communities
  /7day        Generate a 7-day reading plan
  /authors     Show top authors to follow
  /foundation  Show foundational papers
  /gaps        Show research gaps and open problems
  /exit        Exit the program

Follow-up questions you can ask:
  "Show papers after 2020"
  "Why is this paper foundational?"
  "Explain the paper about regret minimization"
  "Find bridge papers between CFR and deep RL"\
""")
