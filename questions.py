questions = {
    "Memory bandwidth": "bytes / second from memory.",

    "VLIW": "Very Long Instruction Word-processor. ILP horny processor.",

    "Score-boarding": """Stores data dependencies of every instruction. Used
    for instruction scheduling.""",

    "Shared-memory architecture": """Several processors share the same
    memory.""",

    "Amdahl's law": """Enhancement E accelerates a fraction F of a program by a
    factor S.  <pre> Speedup = 1/(1-F + F/S) </pre>""",

    "Virtual memory miss": """The memory location is not stored in the TLB and
    a page table walk is required.""",

    "Page walk": """The CPU walks the page tables in order to find the virtual
    address. It is then added to the TLB.""",

    "Bus snooping": """Caches monitor address lines for write accesses to
    memory locations that have been cached. Write invalidate protocol. Used
    for cache coherence.""",

    "Cache coherence": "Shared memory that is cached by multiple caches.",

    "Out-of-order execution": """Instructions are not executed in the same
    order as the original program.""",

    "Inexact exception": """The result of an arithmetic operation on two
    floating-point values can have more significant bits than the destination
    register can contain.""",

    "Memory architecture: Accumulator": """Intermediate calculations are stored
    in an accumulator register.""",

    "Memory architecture: Memory-memory": """No registers are used, all
    instructions fetch from memory directly. Low code size but lots of memory
    accesses.""",

    "Memory architecture: Stack": """Values are stored on a stack, push and pop
    operations. Registers can be used to represent the top of the stack.""",

    "Memory architecture: Load-store": """Only registers are used, memory is
    explicitly fetched using load/store operations.""",

    "CPU Performance Equation (explain terms)": """
    <ul>
    <li>IC (n): Instruction Count.</li>
    <li>CPI (n): Cycles Per Instruction.</li>
    <li>Miss rate (%): Chance to miss a memory access.</li>
    <li>Miss penalty (ns): Cost of a miss.</li>
    <li>Tc (s): Time to execute one instruction</li>
    </ul>""",

    "Execution time (calculate)": """
    <pre>
    IC * (CPIexec + (mem accesses / instructions) * miss rate * miss penalty) * Tc
    </pre>
    """,

    "MFLOPS": "Million Floating Operations Per Second.",

    "Name dependencies (name two kinds)": """Two instructions use same name
    (register or memory address) but do not exchange data.
    <ul>
      <li>Anti-dependence: WAR in HW.</li>
      <li>Output dependence: WAW in HW.</li>
    </ul>""",

    "True dependencies": """Data is transmitted between instructions, RAW.""",

    "Hazards": """Prevents an instruction from being executed.
    <ul>
      <li>Data hazard: Data dependencies between instructions</li>
      <li> Structural hazard: Simultaneous use of a HW resource</li>
      <li>Control hazard: Change in program flow</li>
    </ul>""",

    "5 Classic pipeline stages": """You should know this.
    <ul>
        <li>IF</li>
        <li>ID</li>
        <li>EX</li>
        <li>MEM</li>
        <li>WB</li>
    </ul>""",

    "CPI": "Cycles Per Instruction",

    "dominance": """In a CFG, if all paths to v are through u - then u
    dominates v.""",

    "basic block": """block of instructions without jumps""",

    "inverted page table": """IPT, basically an off-chip TLB. Resides in
    RAM.""",

    "true sharing misses": """Misses arising from communication of data through
    cache coherence mechanism""",

    "register renaming": """A set of physical registers holds both
    architecturally visible register as well as temporary data. During
    instruction issue architectural registers are mapped to physical regsiters.
    Register renaming is used to get rid of WAR and WAW hazards.""",

    "data dependency": """an instruction (i1) is data dependent on another
    instruction (i2) if i2 produces a value needed by i1. It (i1) can also be
    dependent on i2 if there is an instruction (i3) that produces a value
    needed by i2.""",

    "way prediction": """An attempt to predict which block the next cache
    access will go to. It allows you to early set up the multiplexor that
    selects cache block.""",

    "unified cache": "A cache that holds both instructions and data",

    "sequential consistency": """Sequential consistency requires that the
    result of any execution be the same as if the memory accesses executed by
    each processor were kept in program order.""",

    "general purpose register instruction set architecture": """GPR have only
    explicit operands, either memory locations or registers, as opposed to
    implicit operands like stack top or acumulator.""",

    "memory hierarchy": """In real life bigger memory is slower and faster
    memory is more expensive. We want to simultaneously increase the speed and
    decrease the cost. Speed is important because widening the performance gap
    between CPU and memory. Size is important since applications and data sets
    are growing bigger. Use several types of memory with varying speeds
    arranged in a hierarchy that is optimized with respect to the use of
    memory. Mapping functions provide address translations between levels.""",

    "MIMD": """Multiple Instruction (streams), Multiple Data (streams). Each
    processor fetches its own instruction and operates on its own data, and it
    targets task-level parallelism (TLP). In general, MIMD, is more flexible
    than SIMD and thus more general, applicable, but is it inherently more
    expensive than SIMD. MIMD can also exploit data-level parallelism (DLP),
    although the overhead is likely to be higher than SIMD computers.""",

    "SIMD": """Single  Instruction (streams), Multiple Data (streams).  The
    same instruction is executed by multiple processors using different data
    streams. SIMD computers exploit data-level parallelism (DLP) by applying
    the same operations to multiple items of data in parallel. Each processor
    has its own data memory but there is a single instruction memory and
    control processor, which fetches and dispatches instructions""",

    "CDB": """Common data bus, when used with a Reorder Buffer it acts as the
    interface betweent the ROB and the FUs""",

    "\"make the common case fast\"": """Investing in hardware that is used
    often makes the most sense for a general speedup""",

    "locality of reference": """
    <ul>
      <li>Temporal locality - close usage in time</li>
      <li>Spatial locality - close in memory</li>
    </ul>
    By having both close, make caches possible. (If they are far apart, that
    makes it extremely difficult to cache...)
    """,

    "The SPEC benchmark series": """SPEC stands for Standard Performance
    Evaluation Corporation<br>The benchmarks consist of several programs
    released over numerous years to measure performance in computing""",

    "ISA": "Instruction set architecture",

    "Control dependency": """As opposed to hazards, dependencies are part of
    the <b>program</b>. The following example illustrates a control dependency:
    <pre>
      if (test1) s1;
      if (test2) s2;
    </pre>
    s1 is CD on test1. s2 is CD on test2, but not on test1.
    """,

    "Reorder buffer": """
    Used by the Tomasulo algorithm for out-of-order execution. Allows for
    speculative exection using four steps: 
    <ul>
      <li>
        <b>Issue</b> - Get instruction from FP Op Queue, if reservation station
        and reorder buffer slot free, issue instr & send operands & reorder
        buffer nbr for destination
      </li>
      <li>
        <b>Execution</b> - operate on operands (EX), if both operands ready -
        execute. If not, watch CDB for results. When both operands are in
        reservation station: execute
      </li>
      <li>
        <b>Write Result</b> - complete execution. Write on Common Data Bus to await
        all awaiting FUs & reorder buffer; mark reservation station available
      </li>
      <li>
        <b>Commit</b> - update register with reorder result. When instr. is at
        head of reorder buffer & result is present: update register with result
        or write to memory (and remove instruction from ROB).
      </li>
    </ul>""",

    "False sharing": """performance-degrading usage pattern that can arise in
    systems with distributed, coherent caches at the size of the smallest
    resource block managed by the caching mechanism. When a system participant
    attempts to periodically access data that will never be altered by another
    party, but that data shares a cache block with data that is altered, the
    caching protocol may force the first participant to reload the whole unit
    despite a lack of logical necessity.""",

    "Five levels of parallelism (used to increase computer system performance)": """
    <ul>
      <li>Bit-level, more bits - more parallelism</li>
      <li>
        ILP - instruction level parallelism. Parallelism among instructions,
        pipeline, superscalar, dynamic scheduling
      </li>
      <li>
        Loop level - Vector Procssors, software scheduling, compiler technology
      </li>
      <li>
        Thread Level -  multithreading, multicore processors, hyperthreading
      </li>
      <li>
        Program Level - multiprocessor computers, multicomputers, clusters
      </li>
    </ul>
    """,

    "TLB": """Translation look-aside buffer, a cache used by memory management
    hardware to improve virtual address translation speed""",

    "Virtual address": """The address space available to a process. The virtual
    addresses are separate from physical addresses and are mapped by the OS.
    This provides process isolation. Several processes sharing the same
    physical memory. Relocation.""",






    "THE FOUR C:s": ""
}
