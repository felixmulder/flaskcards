questions = {
    "Memory bandwidth": "bytes / second from memory.",
    "VLIW": "Very Long Instruction Word-processor. ILP horny processor.",
    "Score-boarding": "Stores data dependencies of every instruction. Used for instruction scheduling.",
    "Shared-memory architecture": "Several processors share the same memory.",
    "Amdahl's law": "Enhancement E accelerates a fraction F of a program by a factor S.",
    "Virtual memory miss": "The memory location is not stored in the TLB and a page table walk is required.",
    "Page walk": "The CPU walks the page tables in order to find the virtual address. It is then added to the TLB.",
    "Bus snooping": "Caches monitor address lines for write accesses to memory locations that have been cached. "
                    "Write invalidate protocol. Used for cache coherence.",
    "Cache coherence": "Shared memory that is cached by multiple caches.",
    "Out-of-order execution": "Instructions are not executed in the same order as the original program.",
    "Inexact exception": "The result of an arithmetic operation on two floating-point values can have more significant bits than the destination register can contain.",
    "Memory architecture: accumulator": "",
    "Memory architecture: Memory-memory": "",
    "Memory architecture: Stack": "",
    "Memory architecture: Load-store": "",
    "CPU Performance Equation (explain terms)": "",
    "Execution time (calculate)": "",
    "MIPS (calculate)": "",
    "MFLOPS": "",
    "Name dependencies (name two kinds)": "",
    "True dependencies": "",
    "Hazards": "",
    "5 Classic pipeline stages": "",
    "CPI": "",
    "dominance": "",
    "basic block": "",
    "inverted page table": "",
    "true sharing misses": "",
    "register renaming": "",
    "data dependency": "",
    "way prediction": "",
    "unified cache": "",
    "sequential consistency": "",
    "general purpose register instruction set architecture": "",
    "memory hierarchy": "",
    "MIMD": "Multiple Instruction (streams), Multiple Data (streams). 
             Each processor fetches its own instruction and 
             operates on its own data, and it targets task-level parallelism (TLP). In general, MIMD, is more flexible
             than SIMD and thus more general, applicable, but is it inherently more expensive than SIMD. MIMD can also
             exploit data-level parallelism (DLP), although the overhead is likely to be higher than SIMD computers.",
    "SIMD": "Single  Instruction (streams), Multiple Data (streams).
             The same instruction is executed by multiple processors using different data streams. SIMD computers exploit
             data-level parallelism (DLP) by applying the same operations to multiple items of data in parallel. Each processor
             has its own data memory but there is a single instruction memory and control processor, which fetches and dispatches
             instructions",
    "make the common case fast": "",
    "locality of reference": "",
    "The SPEC benchmark series": "",
    "Control dependency": "",
    "Reorder buffer": "",
    "False sharing": "",
    "imprecise exceptions": "",
    "Five levels of parallelism (used to increase computer system performance)": "",
    "TLB": "Translation look-aside buffer, a cache used by memory management hardware to improve virtual address translation speed",
    "Virtual address": "The address space available to a process. The virtual addresses are separate from physical addresses and are mapped by the OS. This provides process isolation. Several processes sharing the same physical memory. Relocation."
}
