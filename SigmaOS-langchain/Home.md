# SigmaOS LangChain

LangChain integration for SigmaOS - LLM application framework.

## Overview

SigmaOS LangChain provides a framework for building applications with large language models. Integration with SigmaOS AI and LLM systems.

## Features

- **LLM applications**: Build LLM-powered applications
- **Chains**: Chain components together
- **Agents**: AI agents
- **Tools**: Tool integration
- **Memory**: Conversation memory
- **Vector stores**: Vector store integration
- **Themes**: SigmaOS theme integration
- **Security**: SigmaOS security integration

## Installation

```bash
sudo pacman -S sigmaos-langchain
```

## Configuration

LangChain is configured to use SigmaOS security policies. Configuration is stored in `~/.config/langchain/`.

## Usage

```python
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Create a chain
prompt = PromptTemplate(template="{question}", input_variables=["question"])
llm = OpenAI()
chain = LLMChain(llm=llm, prompt=prompt)

# Run the chain
result = chain.run(question="What is SigmaOS?")
```

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-langchain)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS Wiki Staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging)
