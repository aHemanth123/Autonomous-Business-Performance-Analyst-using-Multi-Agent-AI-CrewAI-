from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.llm import LLM
from typing import List 


@CrewBase
class BusinessPerformanceCrew:
    """
    Autonomous Business Performance Analyst Crew
    """

    agents: List[BaseAgent]
    tasks: List[Task]

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # =====================
    # AGENTS
    # =====================

    @agent
    def data_ingestion_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["data_ingestion_agent"],
            llm=LLM(model="ollama/llama3.1:latest", temperature=0.2),
            verbose=True
        )

    @agent
    def trend_analysis_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["trend_analysis_agent"],
            llm=LLM(model="ollama/llama3.1:latest", temperature=0.3),
            verbose=True
        )

    @agent
    def anomaly_detection_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["anomaly_detection_agent"],
            llm=LLM(model="ollama/llama3.1:latest", temperature=0.25),
            verbose=True
        )

    @agent
    def business_insight_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["business_insight_agent"],
            llm=LLM(model="ollama/llama3.1:latest", temperature=0.35),
            verbose=True
        )

    @agent
    def report_generator_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["report_generator_agent"],
            llm=LLM(model="ollama/llama3.1:latest", temperature=0.4),
            verbose=True
        )

    # =====================
    # TASKS (EXPLICIT CONTEXT)
    # =====================

    @task
    def load_data_task(self) -> Task:
        return Task(
            config=self.tasks_config["load_data_task"],
            agent=self.data_ingestion_agent()
        )

    @task
    def trend_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config["trend_analysis_task"],
            agent=self.trend_analysis_agent(),
            context=[self.load_data_task()]
        )

    @task
    def anomaly_detection_task(self) -> Task:
        return Task(
            config=self.tasks_config["anomaly_detection_task"],
            agent=self.anomaly_detection_agent(),
            context=[self.load_data_task()]
        )

    @task
    def business_insight_task(self) -> Task:
        return Task(
            config=self.tasks_config["business_insight_task"],
            agent=self.business_insight_agent(),
            context=[
                self.trend_analysis_task(),
                self.anomaly_detection_task()
            ]
        )

    @task
    def report_generation_task(self) -> Task:
     return Task(
        config=self.tasks_config["report_generation_task"],
        agent=self.report_generator_agent(),
        context=[self.business_insight_task()],
        output_file="reports/business_report.pdf"
    )

    # =====================
    # CREW
    # =====================

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=[
                self.load_data_task(),
                self.trend_analysis_task(),
                self.anomaly_detection_task(),
                self.business_insight_task(),
                self.report_generation_task()
            ],
            process=Process.sequential,
            verbose=True
        )
