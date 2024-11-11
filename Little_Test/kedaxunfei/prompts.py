anli_prompt = """There are three kinds of candidate relations: 1. entailment, 2. neutral, 3. contradiction.

Given two sentences \"Premise\" and \"Hypothesis\":

Premise: {Premise}
Hypothesis: {Hypothesis}

Please predit which relation they belong to. And you should only output the index of the target relaton.
"""