from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI
from crewai_tools import PDFSearchTool

import os
from langchain_openai import ChatOpenAI

class CustomAgents:
    def __init__(self):
        OPENAI_API_KEY = "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"
        
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7, openai_api_key=OPENAI_API_KEY)
        self.OpenAIGPT4o = ChatOpenAI(model_name="gpt-4o", temperature=0.7, openai_api_key=OPENAI_API_KEY)

    def pdf_agent(self):
        pdf_tool = PDFSearchTool("gpt-4-analysis.pdf")

        return Agent(
            role="Senior PDF Analyst",
            backstory=dedent(f"""You can find anything in a pdf. The people need you."""),
            goal=dedent(f"""Uncover any information from pdf files exceptionally well."""),
            tools=[pdf_tool],
            verbose=True,
            llm=self.OpenAIGPT4o,
        )

    def writer_agent(self):
        return Agent(
            role="Writer",
            backstory=dedent(f"""All your life you have loved writing summaries."""),
            goal=dedent(f"""Take the information from the pdf agent and summarize it nicely."""),
            verbose=True,
            llm=self.OpenAIGPT35,
        )
