import os
from textwrap import dedent

from crewai import Crew
#from decouple import config

from custom_agents import CustomAgents
from tasks import CustomTasks

#OPENAI_API_KEY = "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"
os.environ["OPENAI_API_KEY"] = "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"


class CustomCrew:
    def __init__(self, var1):
        self.var1 = var1

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = CustomAgents()
        tasks = CustomTasks()

        # Define your custom agents and tasks here
        pdf_agent = agents.pdf_agent()
        writer_agent = agents.writer_agent()

        # Custom tasks include agent name and variables as input
        task1 = tasks.pdf_task(
            pdf_agent,
            self.var1
        )

        task2 = tasks.writer_task(
            writer_agent,
        )

        # Define your custom crew here
        crew = Crew(
            agents=[pdf_agent, writer_agent],
            tasks=[task1, task2],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Crew AI Template")
    print("-------------------------------")
    var1 = input(dedent("""Enter variable 1: """))

    custom_crew = CustomCrew(var1)
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is you custom crew run result:")
    print("########################\n")
    print(result)