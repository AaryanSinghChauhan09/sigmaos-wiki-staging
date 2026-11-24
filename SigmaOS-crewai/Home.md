# SigmaOS CrewAI

CrewAI integration for SigmaOS - multi-agent AI framework.

## Overview

SigmaOS CrewAI provides a multi-agent AI framework for building collaborative AI agents. Integration with SigmaOS AI and agent systems.

## Features

- **Multi-agent**: Multi-agent collaboration
- **Agent roles**: Define agent roles and responsibilities
- **Task management**: Task management and delegation
- **Memory**: Agent memory and context
- **Tools**: Tool integration
- **Themes**: SigmaOS theme integration
- **Security**: SigmaOS security integration
- **Documentation**: Comprehensive documentation

## Installation

```bash
sudo pacman -S sigmaos-crewai
```

## Configuration

CrewAI is configured to use SigmaOS security policies. Configuration is stored in `~/.config/crewai/`.

## Usage

```python
from crewai import Agent, Task, Crew

# Create agents
researcher = Agent(role='Researcher', goal='Research topics', backstory='...')
writer = Agent(role='Writer', goal='Write content', backstory='...')

# Create tasks
task1 = Task(description='Research topic', agent=researcher)
task2 = Task(description='Write article', agent=writer)

# Create crew
crew = Crew(agents=[researcher, writer], tasks=[task1, task2])
result = crew.kickoff()
```

## Links

- [Repository](https://github.com/AaryanSinghChauhan09/SigmaOS-crewai)
- [SigmaOS project](https://github.com/AaryanSinghChauhan09/Sigma)
- [SigmaOS Wiki Staging](https://github.com/AaryanSinghChauhan09/sigmaos-wiki-staging)
