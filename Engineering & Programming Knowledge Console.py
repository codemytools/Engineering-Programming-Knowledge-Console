# ==========================================
# Prototype Module
# ==========================================

class Prototype:

    def __init__(self):

        self.types = {
            "Concept": "Tests ideas and feasibility only.",
            "Visual": "Looks like the final product but may not function.",
            "Functional": "Works correctly but may lack final appearance.",
            "Production": "Looks and functions like the intended final version."
        }

        self.specifications = {
            "Interior": "Wiring, circuits, firmware, mechanical structure.",
            "Exterior": "Shape, layout, surface finish, interface design.",
            "Version": "vX.X (iteration tracking)",
            "Performance Evaluation": "Speed, latency, throughput, accuracy, power usage, stability.",
            "Tech Demonstration": "Proof of concept and controlled performance showcase."
        }

    def display(self):

        print(">>> Types of Prototypes")

        for name, desc in self.types.items():
            print(f"- {name}: {desc}")

        print("\n>>> Prototype Specifications")

        for name, desc in self.specifications.items():
            print(f"- {name}: {desc}")

        print()


# ==========================================
# Skill Domain Module
# ==========================================

class PrototypeSkills:

    def __init__(self):

        self.domains = {
            "Design": "System architecture, UX layout, structural planning.",
            "Electronic": "Circuit design, component integration, signal validation.",
            "Physical/Mechanical": "Material structure, enclosure durability, form stability.",
            "Networking": "Device communication, IoT protocols, data exchange testing.",
            "Programming": "Firmware logic, debugging, state control.",
            "Cloud": "Remote processing, storage integration, scalability validation.",
            "Security": "Encryption, authentication, vulnerability testing."
        }

    def display(self):

        print(">>> Understand Prototyping")

        for name, desc in self.domains.items():
            print(f"- {name}: {desc}")

        print()


# ==========================================
# C Language Notes
# ==========================================

class C_Language:

    def __init__(self):

        self.core_features = {
            "Preprocessing": "#include, #define directives before compilation.",
            "Compilation": "Converts C source code into object code.",
            "Linking": "Combines objects and libraries into executable.",
            "Execution": "Program runs on operating system.",
            "Debugging": "Tracing runtime errors and memory issues."
        }

        self.modes = {
            "Snippet Testing": "Small compile-run cycles for testing logic.",
            "Program Mode": "Writing full .c programs."
        }

        self.key_concepts = {
            "Data Types": "int, float, double, char, void",
            "Control Flow": "if, else, switch, while, for",
            "Functions": "Reusable blocks with arguments and returns",
            "Pointers": "Variables holding memory addresses",
            "Structs": "Custom grouped data types",
            "Memory": "Stack vs Heap (malloc/free)",
            "File I/O": "fopen, fread, fwrite"
        }

    def display(self):

        print(">>> C Language")

        print("\nCore Features")

        for name, desc in self.core_features.items():
            print(f"- {name}: {desc}")

        print("\nModes")

        for name, desc in self.modes.items():
            print(f"- {name}: {desc}")

        print("\nKey Concepts")

        for name, desc in self.key_concepts.items():
            print(f"- {name}: {desc}")

        print()

      # ==========================================
# C++ Language Notes
# ==========================================

class CPP_Language:

    def __init__(self):

        self.core_features = {
            "Compilation Model": "C++ is compiled into native machine code via compiler (g++/clang++) with strong optimization pipelines.",
            "Abstraction Layer": "Supports high-level constructs (classes, templates) while still allowing low-level memory control.",
            "Performance": "Near-C level performance with additional structure for scalable systems.",
            "Standard Library (STL)": "Provides containers (vector, map), algorithms, and utilities for fast development.",
            "Cross-Language Foundation": "Core backend language for major AI frameworks (PyTorch, TensorFlow runtime, ONNX)."
        }

        self.modes = {
            "System Development": "Used for engines, OS components, and high-performance backend systems.",
            "AI Framework Core": "Implements tensor operations, graph execution, and model runtime logic.",
            "Embedded + Edge AI": "Runs optimized inference on constrained devices (robotics, IoT, mobile AI)."
        }

        self.key_concepts = {
            "Object-Oriented Programming": "Encapsulation, inheritance, polymorphism for modular system design.",
            "Templates": "Generic programming enabling reusable high-performance components.",
            "Memory Management": "Manual + smart pointers (unique_ptr, shared_ptr) for controlled allocation.",
            "Concurrency": "Multithreading and parallel execution (std::thread, async).",
            "Hardware Proximity": "Can operate close to system level (similar to C but with structure).",
            "GPU / AI Backends": "Interfaces with CUDA and compute kernels for AI acceleration."
        }

    def display(self):

        print(">>> C++ Language")

        print("\nCore Features")

        for name, desc in self.core_features.items():
            print(f"- {name}: {desc}")

        print("\nModes")

        for name, desc in self.modes.items():
            print(f"- {name}: {desc}")

        print("\nKey Concepts")

        for name, desc in self.key_concepts.items():
            print(f"- {name}: {desc}")

        print()

 # ==========================================
# Rust Language Notes
# ==========================================

class Rust_Language:

    def __init__(self):

        self.core_features = {
            "Memory Model": "Deterministic memory control using ownership system (no garbage collector).",
            "Compile-Time Safety": "Errors caught at compile time instead of runtime execution.",
            "Zero-Cost Abstractions": "High-level constructs compile down to near C-level performance.",
            "Concurrency Safety": "Prevents data races through ownership + borrowing rules.",
            "Performance Profile": "Optimized for systems-level execution with minimal runtime overhead."
        }

        self.modes = {
            "Systems Programming": "Operating systems, kernels, embedded systems, performance-critical software.",
            "Interface Layer Development": "WASM modules, CLI tools, API gateways, edge services.",
            "Performance-Critical Components": "Hot paths where latency and predictability matter most."
        }

        self.key_concepts = {
            "Ownership System": "Each value has a single owner controlling memory lifecycle.",
            "Borrowing Rules": "Safe references without data races or invalid memory access.",
            "Lifetimes": "Compile-time tracking of reference validity.",
            "Traits": "Interface-like abstraction system for behavior composition.",
            "No Garbage Collector": "Memory is managed deterministically by the compiler.",
            "Strict Compilation": "Prevents unsafe or ambiguous runtime behavior."
        }

    def display(self):

        print(">>> Rust Language")

        print("\nCore Features")

        for name, desc in self.core_features.items():
            print(f"- {name}: {desc}")

        print("\nModes")

        for name, desc in self.modes.items():
            print(f"- {name}: {desc}")

        print("\nKey Concepts")

        for name, desc in self.key_concepts.items():
            print(f"- {name}: {desc}")

        print()     

# ==========================================
# Java Language Notes
# ==========================================

class Java_Language:

    def __init__(self):

        self.core_features = {
            "Static Typing": "Strict type declarations enforced at compile-time to prevent invalid operations.",
            "Memory Safety": "No direct pointer access; prevents manual memory corruption.",
            "Garbage Collection": "Automatic memory management reduces leaks and manual cleanup errors.",
            "JVM Execution": "Runs on Java Virtual Machine with bytecode verification and sandboxing.",
            "Object-Oriented Structure": "Everything organized into classes with enforced modular design.",
            "Checked Exceptions": "Forces explicit handling or declaration of runtime-risk operations."
        }

        self.modes = {
            "Application Development": "Structured development for large-scale systems and services.",
            "Backend Services": "Long-running server-side applications and APIs.",
            "Cross-Platform Execution": "Write once, run anywhere via JVM."
        }

        self.key_concepts = {
            "Classes & Objects": "Blueprint-based system design with encapsulation.",
            "Interfaces": "Contracts that enforce consistent implementation across systems.",
            "Inheritance & Polymorphism": "Extensible and reusable architecture patterns.",
            "JVM & Bytecode": "Intermediate execution layer enabling portability and control.",
            "Multithreading": "Built-in concurrency support for scalable systems.",
            "Packages": "Namespace organization for large codebases.",
            "Exception Handling": "try/catch system enforcing error management discipline."
        }

    def display(self):

        print(">>> Java Language")

        print("\nCore Features")

        for name, desc in self.core_features.items():
            print(f"- {name}: {desc}")

        print("\nModes")

        for name, desc in self.modes.items():
            print(f"- {name}: {desc}")

        print("\nKey Concepts")

        for name, desc in self.key_concepts.items():
            print(f"- {name}: {desc}")

        print()
      
# ==========================================
# Python IDLE
# ==========================================

class IDLE:

    def __init__(self):

        self.core_features = {
            "Interpret": "Interactive shell.",
            "Edit": "Code editor with auto-indent.",
            "Orchestrate": "File management.",
            "Inspect": "Debugger and namespace viewer.",
            "Dialog": "Preferences and module browser."
        }

        self.modes = {
            "Shell": "Experimenting and testing.",
            "Script": "Structured program development."
        }

        self.limits = [
            "Hard real-time guarantees are not reliable",
            "Strict concurrency control is limited at scale (GIL constraints in CPython)",
            "Deterministic performance is not guaranteed due to interpreter overhead",
            "Memory-critical coordination is less efficient compared to compiled languages",
            "Ultra-low latency pipelines require external optimized extensions (C/C++/Rust)"
        ]

    def display(self):

        print(">>> Python v3.x")

        print("\nIDLE")
        for name, desc in self.core_features.items():
            print(f"- {name}: {desc}")

        print("\nModes")
        for name, desc in self.modes.items():
            print(f"- {name}: {desc}")

        print("\nLimits")
        for item in self.limits:
            print(f"- {item}")

        print()
# ==========================================
# React
# ==========================================

class React_Library:

    def __init__(self):

        self.core_features = {
            "Components": "Reusable UI building blocks (functional or class-based).",
            "JSX": "JavaScript syntax extension that looks like HTML.",
            "State": "Internal data that controls component behavior.",
            "Props": "Inputs passed to components for dynamic rendering.",
            "Lifecycle": "Methods/hooks controlling component mount/update/unmount.",
            "Virtual DOM": "Efficient diffing and rendering system.",
            "Hooks": "Functions like useState, useEffect for functional components."
        }

        self.modes = {
            "Development": "Local dev server with hot-reloading for rapid iteration.",
            "Production": "Optimized build for deployment."
        }

        self.key_concepts = {
            "Unidirectional Data Flow": "Data flows from parent to child components.",
            "Component Composition": "Combining small components into complex UIs.",
            "Event Handling": "Managing user interactions with callbacks and synthetic events.",
            "Conditional Rendering": "Render UI elements based on state or props.",
            "Forms & Controlled Components": "Handle form inputs with state binding.",
            "Routing": "Navigation between views using React Router.",
            "Context API": "Global state sharing without prop drilling."
        }

    def display(self):

        print(">>> React Library")

        print("\nCore Features")
        for name, desc in self.core_features.items():
            print(f"- {name}: {desc}")

        print("\nModes")
        for name, desc in self.modes.items():
            print(f"- {name}: {desc}")

        print("\nKey Concepts")
        for name, desc in self.key_concepts.items():
            print(f"- {name}: {desc}")

        print()

# ==========================================
# Embedded Systems Module
# ==========================================

class EmbeddedSystems:
    def __init__(self):

        self.domains = {
            "Motor Control": "Closed-loop tuning for robotics, drones, CNC systems.",
            "Audio Systems": "Amplifiers and analog signal integrity management.",
            "Sensor Calibration": "ADC tuning, scaling, and tolerance validation.",
            "Power Management": "Feedback loop stability and voltage regulation.",
            "Debugging": "Datasheet interpretation and real-world validation."
        }

        self.operational_pattern = [
            "Open spec sheet",
            "Adjust parameters (analog/register)",
            "Measure response",
            "Compare to target/spec",
            "Iterate systematically"
        ]

        self.meta_skill = [
            "Working inside constraints",
            "Interpreting documentation precisely",
            "Adjusting variables systematically",
            "Avoiding guess-based tuning",
            "Thinking in ranges, not absolutes",
            "Closed-loop calibration thinking under constraint"
        ]

        self.skill_transfer = [
            "Firmware engineering",
            "Hardware prototyping",
            "IoT systems",
            "Automotive ECUs",
            "Medical device firmware"
        ]

        self.software_analogy = {
            "Adjust PWM": "Adjust model parameters",
            "Compare to brightness spec": "Compare to fair-pricing model",
            "Stay within voltage limits": "Stay within risk limits",
            "Real-time feedback": "Market feedback"
        }

    def display(self):
        print(">>> Embedded Systems")

        print("\nCore Domains:")
        for name, desc in self.domains.items():
            print(f"- {name}: {desc}")

        print("\nOperational Pattern:")
        for step in self.operational_pattern:
            print(f"- {step}")

        print("\nMeta Skills Being Trained:")
        for skill in self.meta_skill:
            print(f"- {skill}")

        print("\nSkill Transfer Into:")
        for domain in self.skill_transfer:
            print(f"- {domain}")

        print("\nSoftware Analogy:")
        for k, v in self.software_analogy.items():
            print(f"- {k}")
            print(f"    --> {v}")
        print()

# ==========================================
# Distributed Data Processing Module
# ==========================================

class DistributedProcessing:
    def __init__(self):

        self.distributed_systems = {
            "Data Partitioning": "Split large datasets into chunks.",
            "Parallel Processing": "Multiple nodes process data simultaneously.",
            "Result Aggregation": "Merge outputs into unified result.",
            "Coordinator": "Manages flow and synchronization."
        }

        self.agentic_ai = {
            "Planner Agent": "Defines strategy and task flow.",
            "Research Agent": "Collects necessary information.",
            "Code Agent": "Executes implementation logic.",
            "Verifier Agent": "Validates correctness.",
            "Memory Manager": "Maintains context consistency.",
            "Execution Module": "Performs actions in environment."
        }

        self.analogy_map = {
            "Data partitioned": "Tasks partitioned",
            "Nodes process chunks": "Agents process subtasks",
            "Results merged": "Outputs synthesized",
            "Coordinator manages flow": "Controller orchestrates modules"
        }

        self.key_distinction = {
            "Distributed computing": "Increases throughput",
            "Agentic AI": "Increases decision depth & autonomy"
        }

        self.failure_handling = {
            "Distributed Systems": [
                "Fault tolerance",
                "Node failure handling",
                "Synchronization control",
                "Consistency models"
            ],
            "Agentic AI": [
                "Reasoning conflicts",
                "Tool failure",
                "Memory corruption",
                "Misaligned subgoals"
            ]
        }

    def display(self):
        print(">>> Distributed Data Processing")

        print("\nDistributed Systems Core:")
        for name, desc in self.distributed_systems.items():
            print(f"- {name}: {desc}")

        print("\nAgentic AI Structure:")
        for name, desc in self.agentic_ai.items():
            print(f"- {name}: {desc}")

        print("\nAnalogy Map:")
        for k, v in self.analogy_map.items():
            print(f"- {k}")
            print(f"    --> {v}")
        print()

        print("Key Distinction:")
        for k, v in self.key_distinction.items():
            print(f"- {k}: {v}")
        print()

        print("Failure Handling Comparison:")
        for system, items in self.failure_handling.items():
            print(f"- {system}:")
            for item in items:
                print(f"    • {item}")
        print()

# ==========================================
# System Controller
# ==========================================

class PrototypeSystem:

    def __init__(self):

        # Add React here along with the other modules
        self.modules = {
            "prototype": Prototype(),
            "skills": PrototypeSkills(),
            "c": C_Language(),
            "cpp": CPP_Language(),
            "rust": Rust_Language(),
            "java": Java_Language(),
            "python": IDLE(),
            "react": React_Library(),
            "embedded": EmbeddedSystems(),
            "distributed": DistributedProcessing()
        }

    def menu(self):
        print("\n=== Engineering & Programming Notes ===\n")
        for name in self.modules:
            print(f"- {name}")
        print("\nType module name or 'exit'\n")

    def run(self):
        while True:
            self.menu()
            choice = input("Select module: ").lower()
            if choice == "exit":
                print("\nExiting...\n")
                break
            if choice in self.modules:
                print()
                self.modules[choice].display()
            else:
                print("Unknown module\n")


# ==========================================
# Execution
# ==========================================

if __name__ == "__main__":
    system = PrototypeSystem()
    system.run()