import asyncio

from temporalio.client import Client
from workflows import GreetingWorkflow


async def main():
    client = await Client.connect("localhost:7233")
    result = await client.execute_workflow(
        GreetingWorkflow.run,
        "World",
        id="periodic-child-workflow-retry",
        task_queue="periodic-retry-task-queue",
    )
    print(f"Result: {result}")


if __name__ == "__main__":
    asyncio.run(main())
