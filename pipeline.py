from agents import (
    build_reader_agent,
    build_search_agent,
    writer_chain,
    critic_chain
)


def run_research_pipeline(topic: str) -> dict:

    state = {}

    # STEP 1 - SEARCH AGENT
    print("\n" + "=" * 50)
    print("STEP 1 - Search agent is working ...")
    print("=" * 50)

    search_agent = build_search_agent()

    search_result = search_agent.invoke({
        "messages": [
            ("user", f"Find recent, reliable and detailed information about: {topic}")
        ]
    })

    # Extract Tavily tool output (contains URLs)
    state["search_results"] = ""

    for msg in search_result["messages"]:
        if hasattr(msg, "name") and msg.name == "web_search":
            state["search_results"] = msg.content
            break

    print("\nSEARCH RESULTS:\n")
    print(state["search_results"])

    # STEP 2 - READER AGENT
    print("\n" + "=" * 50)
    print("STEP 2 - Reader agent is scraping top resources ...")
    print("=" * 50)

    reader_agent = build_reader_agent()

    reader_result = reader_agent.invoke({
        "messages": [(
            "user",
            f"""
            Based on the following search results about '{topic}',

            1. Identify the most authoritative and relevant URL.
            2. Use the scrape_url tool to scrape that URL.
            3. Return the scraped content only.

            Search Results:

            {state["search_results"]}
            """
        )]
    })

    state["scraped_content"] = reader_result["messages"][-1].content

    print("\nSCRAPED CONTENT:\n")
    print(state["scraped_content"])

    # STEP 3 - WRITER CHAIN
    print("\n" + "=" * 50)
    print("STEP 3 - Writer is drafting the report ...")
    print("=" * 50)

    research_combined = (
        f"SEARCH RESULTS:\n{state['search_results']}\n\n"
        f"SCRAPED CONTENT:\n{state['scraped_content']}"
    )

    state["report"] = writer_chain.invoke({
        "topic": topic,
        "research": research_combined
    })

    print("\nFINAL REPORT:\n")
    print(state["report"])

    # STEP 4 - CRITIC CHAIN
    print("\n" + "=" * 50)
    print("STEP 4 - Critic is reviewing the report ...")
    print("=" * 50)

    state["feedback"] = critic_chain.invoke({
        "report": state["report"]
    })

    print("\nCRITIC FEEDBACK:\n")
    print(state["feedback"])

    return state


if __name__ == "__main__":
    topic = input("\nEnter a research topic: ")
    run_research_pipeline(topic)