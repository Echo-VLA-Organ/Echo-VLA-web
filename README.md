# EchoVLA: Robotic Vision-Language-Action Model with Synergistic Declarative Memory for Mobile Manipulation

## Overview
EchoVLA is a memory-aware Vision-Language-Action (VLA) model designed for long-horizon mobile manipulation tasks. Unlike existing VLAs that are mostly confined to short-horizon, table-top manipulation, EchoVLA incorporates a **synergistic declarative memory** system inspired by the human brain, enabling consistent reasoning over extended task sequences and long-term spatial understanding.

The model introduces two complementary memory modules: a **Scene Memory** that maintains spatial-semantic maps across different scenes, and an **Episodic Memory** that stores task-level experiences with multimodal contextual features. These memories are independently stored, updated, and retrieved during both training and inference, with their representations fused through coarse- and fine-grained attention to guide mobile-arm diffusion policies.

Additionally, EchoVLA is validated using **MoMani**, an automated benchmark that generates expert-level long-horizon trajectories through multimodal large language model (MLLM)–guided planning and feedback-driven refinement, supplemented with real-robot demonstrations.

## Key Features
- **Dual Memory System**: Scene memory for spatial-semantic understanding and episodic memory for task-level experiences.
- **Memory-Guided Attention**: Coarse attention over scene memory and fine attention over episodic memory for context-aware action generation.
- **MoMani Benchmark**: Automated benchmark providing expert-level multimodal trajectories and real-robot demonstrations.
- **Long-Horizon Mobile Manipulation**: Achieves state-of-the-art performance on manipulation/navigation tasks (0.52 success rate) and mobile manipulation tasks (0.31 success rate).
