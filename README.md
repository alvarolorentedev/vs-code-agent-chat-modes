# <img width="350" alt="VS Code Agent Chat Modes" src="https://github.com/user-attachments/assets/baadc49d-87e2-41de-83be-a7bac7db0483" />
 
A comprehensive collection of specialized AI agents designed to accelerate and enhance every aspect of rapid development. Each agent is an expert in their domain, ready to be invoked when their expertise is needed.

based on [contains-studio/agents](https://github.com/contains-studio/agents)

## 📥 Installation

1. **Download this repository:**
   ```bash
   git clone https://github.com/contains-studio/agents.git
   ```

2. **Copy to your chat modes agents directory:**
   ```bash
   cp -r modes/* ~/.config/Code/User/prompts
   ```

   Or manually copy all the agent files to your vscode `~/.config/Code/User/prompts` directory.

## 🚀 Quick Start

Chat modes Agents are automatically available in vs code. Select the agent and provide a task.

📚 **Learn more:** [vs code chat modes Documentation](hhttps://code.visualstudio.com/docs/copilot/chat/chat-modes)

### Example Usage
- "Create a new app for tracking meditation habits" → `rapid-prototyper`
- "What's trending on TikTok that we could build?" → `trend-researcher`
- "Our app reviews are dropping, what's wrong?" → `feedback-synthesizer`
- "Make this loading screen more fun" → `whimsy-injector`

## 📋 Complete Agent List

### Engineering Department (`[engineering]`)
- **[engineering] ai-engineer** - Integrate AI/ML features that actually ship
- **[engineering] devops-automator** - Deploy continuously without breaking things
- **[engineering] backend-architect** - Design scalable APIs and server systems
- **[engineering] frontend-developer** - Build blazing-fast user interfaces
- **[engineering] mobile-app-builder** - Create native iOS/Android experiences
- **[engineering] rapid-prototyper** - Build MVPs in days, not weeks
- **[engineering] test-writer-fixer** - Write tests that catch real bugs

### Product Department (`[product]`)
- **[product] feedback-synthesizer** - Transform complaints into features
- **[product] sprint-prioritizer** - Ship maximum value in 6 days
- **[product] trend-researcher** - Identify viral opportunities

### Marketing Department (`[marketing]`)
- **[marketing] app-store-optimizer** - Dominate app store search results
- **[marketing] content-creator** - Generate content across all platforms
- **[marketing] growth-hacker** - Find and exploit viral growth loops
- **[marketing] instagram-curator** - Master the visual content game
- **[marketing] reddit-community-builder** - Win Reddit without being banned
- **[marketing] tiktok-strategist** - Create shareable marketing moments
- **[marketing] twitter-engager** - Ride trends to viral engagement

### Design Department (`[design]`)
- **[design] brand-guardian** - Keep visual identity consistent everywhere
- **[design] ui-designer** - Design interfaces developers can actually build
- **[design] ux-researcher** - Turn user insights into product improvements
- **[design] visual-storyteller** - Create visuals that convert and share
- **[design] whimsy-injector** - Add delight to every interaction

### Project Management (`[project-management]`)
- **[project-management] experiment-tracker** - Data-driven feature validation
- **[project-management] project-shipper** - Launch products that don't crash
- **[project-management] studio-producer** - Keep teams shipping, not meeting

### Studio Operations (`[studio-operations]`)
- **[studio-operations] analytics-reporter** - Turn data into actionable insights
- **[studio-operations] finance-tracker** - Keep the studio profitable
- **[studio-operations] infrastructure-maintainer** - Scale without breaking the bank
- **[studio-operations] legal-compliance-checker** - Stay legal while moving fast
- **[studio-operations] support-responder** - Turn angry users into advocates

### Testing & Benchmarking (`[testing]`)
- **[testing] api-tester** - Ensure APIs work under pressure
- **[testing] performance-benchmarker** - Make everything faster
- **[testing] test-results-analyzer** - Find patterns in test failures
- **[testing] tool-evaluator** - Choose tools that actually help
- **[testing] workflow-optimizer** - Eliminate workflow bottlenecks

### Bonus Agents  (`[bonus]`)
- **[bonus] studio-coach** - Rally the AI troops to excellence
- **[bonus] joker** - Lighten the mood with tech humor


## 💡 Best Practices

1. **Be specific** - Clear task descriptions help agents perform better.
2. **Trust the expertise** - Agents are designed for their specific domains.
3. **Iterate quickly** - Agents support the 6-day sprint philosophy.

## 🔧 Technical Details

### Agent Structure
Each agent includes:
- **description**: When to use the agent with examples
- **tools**: Specific tools the agent can access
- **System prompt**: Detailed expertise and instructions

### Adding New Agents
1. Create a new `.chatmode.md` file with the appropriate name `[department]`
2. Follow the existing format with YAML frontmatter
3. Include 3-4 detailed usage examples
4. Write comprehensive system prompt (500+ words)
5. Test the agent with real tasks

## 📊 Agent Performance

Track agent effectiveness through:
- Task completion time
- User satisfaction
- Error rates
- Feature adoption
- Development velocity

## 🚦 Status

- ✅ **Active**: Fully functional and tested
- 🚧 **Coming Soon**: In development
- 🧪 **Beta**: Testing with limited functionality

## 🛠️ Customizing Agents for Your Studio

### Agent Customization Todo List

Use this checklist when creating or modifying agents for your specific needs:

#### 📋 Required Components
- [ ] **YAML Frontmatter**
  - [ ] `description`: When to use + 3-4 detailed examples with context/commentary
  - [ ] `tools`: Specific tools the agent can access (Write, Read, MultiEdit, Bash, etc.)

#### 📝 System Prompt Requirements (500+ words)
- [ ] **Agent Identity**: Clear role definition and expertise area
- [ ] **Core Responsibilities**: 5-8 specific primary duties
- [ ] **Domain Expertise**: Technical skills and knowledge areas
- [ ] **Studio Integration**: How agent fits into 6-day sprint workflow
- [ ] **Best Practices**: Specific methodologies and approaches
- [ ] **Constraints**: What the agent should/shouldn't do
- [ ] **Success Metrics**: How to measure agent effectiveness

#### 🎯 Required Examples by Agent Type

**Engineering Agents** need examples for:
- [ ] Feature implementation requests
- [ ] Bug fixing scenarios
- [ ] Code refactoring tasks
- [ ] Architecture decisions

**Design Agents** need examples for:
- [ ] New UI component creation
- [ ] Design system work
- [ ] User experience problems
- [ ] Visual identity tasks

**Marketing Agents** need examples for:
- [ ] Campaign creation requests
- [ ] Platform-specific content needs
- [ ] Growth opportunity identification
- [ ] Brand positioning tasks

**Product Agents** need examples for:
- [ ] Feature prioritization decisions
- [ ] User feedback analysis
- [ ] Market research requests
- [ ] Strategic planning needs

**Operations Agents** need examples for:
- [ ] Process optimization
- [ ] Tool evaluation
- [ ] Resource management
- [ ] Performance analysis

#### ✅ Testing & Validation Checklist
- [ ] **Trigger Testing**: Agent activates correctly for intended use cases
- [ ] **Tool Access**: Agent can use all specified tools properly
- [ ] **Output Quality**: Responses are helpful and actionable
- [ ] **Edge Cases**: Agent handles unexpected or complex scenarios
- [ ] **Integration**: Works well with other agents in multi-agent workflows
- [ ] **Performance**: Completes tasks within reasonable timeframes
- [ ] **Documentation**: Examples accurately reflect real usage patterns

#### 🔧 Agent File Structure Template

```markdown
---
description: Use this agent when [scenario]. This agent specializes in [expertise]. Examples:\n\n<example>\nContext: [situation]\nuser: "[user request]"\nassistant: "[response approach]"\n<commentary>\n[why this example matters]\n</commentary>\n</example>\n\n[3 more examples...]
tools: Tool1, Tool2, Tool3
---

You are a [role] who [primary function]. Your expertise spans [domains]. You understand that in 6-day sprints, [sprint constraint], so you [approach].

Your primary responsibilities:
1. [Responsibility 1]
2. [Responsibility 2]
...

[Detailed system prompt content...]

Your goal is to [ultimate objective]. You [key behavior traits]. Remember: [key philosophy for 6-day sprints].
```

#### 📂 Department-Specific Guidelines

**Engineering** (`engineering/`): Focus on implementation speed, code quality, testing
**Design** (`design/`): Emphasize user experience, visual consistency, rapid iteration  
**Marketing** (`marketing/`): Target viral potential, platform expertise, growth metrics
**Product** (`product/`): Prioritize user value, data-driven decisions, market fit
**Operations** (`studio-operations/`): Optimize processes, reduce friction, scale systems
**Testing** (`testing/`): Ensure quality, find bottlenecks, validate performance
**Project Management** (`project-management/`): Coordinate teams, ship on time, manage scope

#### 🎨 Customizations

Modify these elements for your needs:
- [ ] Adjust examples to reflect your product types
- [ ] Add specific tools agents have access to
- [ ] Modify success metrics for your KPIs
- [ ] Update department structure if needed
- [ ] Customize agent colors for your brand

## 🤝 Contributing

To improve existing agents or suggest new ones:
1. Use the customization checklist above
2. Test thoroughly with real projects
3. Document performance improvements
4. Share successful patterns with the community
