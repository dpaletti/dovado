LIBRARY IEEE;
USE IEEE.Std_logic_1164.ALL;
-- FPGA projects using VHDL/ VHDL fpga4student.com VHDL code for FIFO memory
ENTITY fifo_mem IS
    GENERIC(
        fake : positive := 4
    );
    PORT(
        data_out : OUT std_logic_vector(7 DOWNTO 0);
        fifo_full : OUT std_logic;
        fifo_empty : OUT std_logic;
        fifo_threshold : OUT std_logic;
        fifo_overflow : OUT std_logic;
        fifo_underflow : OUT std_logic;
        clk : IN std_logic;
        rst_n : IN std_logic;
        wr : IN std_logic;
        rd : IN std_logic;
        data_in : IN std_logic_vector(7 DOWNTO 0)
    );
END ENTITY;

ARCHITECTURE Behavioral OF fifo_mem IS
    COMPONENT write_pointer IS
        PORT(
            wptr : OUT std_logic_vector(4 DOWNTO 0);
            fifo_we : OUT std_logic;
            clk : IN std_logic;
            rst_n : IN std_logic;
            wr : IN std_logic;
            fifo_full : IN std_logic
        );
    END COMPONENT;
    COMPONENT read_pointer IS
        PORT(
            rptr : OUT std_logic_vector(4 DOWNTO 0);
            fifo_rd : OUT std_logic;
            clk : IN std_logic;
            rst_n : IN std_logic;
            rd : IN std_logic;
            fifo_empty : IN std_logic
        );
    END COMPONENT;
    COMPONENT memory_array IS
        PORT(
            data_out : OUT std_logic_vector(7 DOWNTO 0);
            rptr : IN std_logic_vector(4 DOWNTO 0);
            clk : IN std_logic;
            fifo_we : IN std_logic;
            wptr : IN std_logic_vector(4 DOWNTO 0);
            data_in : IN std_logic_vector(7 DOWNTO 0)
        );
    END COMPONENT;
    COMPONENT status_signal IS
        PORT(
            fifo_full : OUT std_logic;
            fifo_empty : OUT std_logic;
            fifo_threshold : OUT std_logic;
            fifo_overflow : OUT std_logic;
            fifo_underflow : OUT std_logic;
            wr : IN std_logic;
            rd : IN std_logic;
            fifo_we : IN std_logic;
            fifo_rd : IN std_logic;
            clk : IN std_logic;
            rst_n : IN std_logic;
            wptr : IN std_logic_vector(4 DOWNTO 0);
            rptr : IN std_logic_vector(4 DOWNTO 0)
        );
    END COMPONENT;
    SIGNAL empty : std_logic;
    SIGNAL full : std_logic;
    SIGNAL wptr : std_logic_vector(4 DOWNTO 0);
    SIGNAL rptr : std_logic_vector(4 DOWNTO 0);
    SIGNAL fifo_we : std_logic;
    SIGNAL fifo_rd : std_logic;
BEGIN
    write_pointer_unit: write_pointer PORT MAP(
        wptr => wptr,
        fifo_we => fifo_we,
        wr => wr,
        fifo_full => full,
        clk => clk,
        rst_n => rst_n
    );
    read_pointer_unit: read_pointer PORT MAP(
        rptr => rptr,
        fifo_rd => fifo_rd,
        rd => rd,
        fifo_empty => empty,
        clk => clk,
        rst_n => rst_n
    );
    memory_array_unit: memory_array PORT MAP(
        data_out => data_out,
        data_in => data_in,
        clk => clk,
        fifo_we => fifo_we,
        wptr => wptr,
        rptr => rptr
    );
    status_signal_unit: status_signal PORT MAP(
        fifo_full => full,
        fifo_empty => empty,
        fifo_threshold => fifo_threshold,
        fifo_overflow => fifo_overflow,
        fifo_underflow => fifo_underflow,
        wr => wr,
        rd => rd,
        fifo_we => fifo_we,
        fifo_rd => fifo_rd,
        wptr => wptr,
        rptr => rptr,
        clk => clk,
        rst_n => rst_n
    );
    fifo_empty <= empty;
    fifo_full <= full;
END ARCHITECTURE;
LIBRARY IEEE;
USE IEEE.Std_logic_1164.ALL;
USE ieee.std_logic_arith.ALL;
USE ieee.std_logic_unsigned.ALL;
-- FPGA projects using VHDL/ VHDL fpga4student.com VHDL code for FIFO memory status signals
ENTITY status_signal IS
    PORT(
        fifo_full : OUT std_logic;
        fifo_empty : OUT std_logic;
        fifo_threshold : OUT std_logic;
        fifo_overflow : OUT std_logic;
        fifo_underflow : OUT std_logic;
        wr : IN std_logic;
        rd : IN std_logic;
        fifo_we : IN std_logic;
        fifo_rd : IN std_logic;
        clk : IN std_logic;
        rst_n : IN std_logic;
        wptr : IN std_logic_vector(4 DOWNTO 0);
        rptr : IN std_logic_vector(4 DOWNTO 0)
    );
END ENTITY;

ARCHITECTURE Behavioral OF status_signal IS
    SIGNAL fbit_comp : std_logic;
    SIGNAL overflow_set : std_logic;
    SIGNAL underflow_set : std_logic;
    SIGNAL pointer_equal : std_logic;
    SIGNAL pointer_result : std_logic_vector(4 DOWNTO 0);
    SIGNAL full : std_logic;
    SIGNAL empty : std_logic;
BEGIN
    fbit_comp <= wptr(4) XOR rptr(4);
    pointer_equal <= '1' WHEN (wptr(3 DOWNTO 0) = rptr(3 DOWNTO 0)) ELSE '0';
    pointer_result <= wptr - rptr;
    overflow_set <= full AND wr;
    underflow_set <= empty AND rd;
    full <= fbit_comp AND pointer_equal;
    empty <= NOT fbit_comp AND pointer_equal;
    fifo_threshold <= '1' WHEN ((pointer_result(4) OR pointer_result(3)) = '1') ELSE '0';
    fifo_full <= full;
    fifo_empty <= empty;
    PROCESS(clk, rst_n)
    BEGIN
        IF rst_n = '0' THEN
            fifo_overflow <= '0';
        ELSIF rising_edge(clk) THEN
            IF overflow_set = '1' AND fifo_rd = '0' THEN
                fifo_overflow <= '1';
            ELSIF fifo_rd = '1' THEN
                fifo_overflow <= '0';
            END IF;
        END IF;
    END PROCESS;
    PROCESS(clk, rst_n)
    BEGIN
        IF rst_n = '0' THEN
            fifo_underflow <= '0';
        ELSIF rising_edge(clk) THEN
            IF underflow_set = '1' AND fifo_we = '0' THEN
                fifo_underflow <= '1';
            ELSIF fifo_we = '1' THEN
                fifo_underflow <= '0';
            END IF;
        END IF;
    END PROCESS;
END ARCHITECTURE;
LIBRARY IEEE;
USE IEEE.Std_logic_1164.ALL;
USE ieee.numeric_std.ALL;
-- FPGA projects using VHDL/ VHDL fpga4student.com VHDL code for FIFO memory Memory array
ENTITY memory_array IS
    PORT(
        data_out : OUT std_logic_vector(7 DOWNTO 0);
        rptr : IN std_logic_vector(4 DOWNTO 0);
        clk : IN std_logic;
        fifo_we : IN std_logic;
        wptr : IN std_logic_vector(4 DOWNTO 0);
        data_in : IN std_logic_vector(7 DOWNTO 0)
    );
END ENTITY;

ARCHITECTURE Behavioral OF memory_array IS
    TYPE mem_array IS ARRAY (0 TO 15) OF std_logic_vector(7 DOWNTO 0);
    SIGNAL data_out2 : mem_array;
BEGIN
    PROCESS(clk)
    BEGIN
        IF rising_edge(clk) THEN
            IF fifo_we = '1' THEN
                data_out2(to_integer(unsigned(wptr(3 DOWNTO 0)))) <= data_in;
            END IF;
        END IF;
    END PROCESS;
    data_out <= data_out2(to_integer(unsigned(rptr(3 DOWNTO 0))));
END ARCHITECTURE;
LIBRARY IEEE;
USE IEEE.Std_logic_1164.ALL;
USE ieee.std_logic_arith.ALL;
USE ieee.std_logic_unsigned.ALL;
-- FPGA projects using VHDL/ VHDL fpga4student.com VHDL code for FIFO memory Read pointer
ENTITY read_pointer IS
    PORT(
        rptr : OUT std_logic_vector(4 DOWNTO 0);
        fifo_rd : OUT std_logic;
        clk : IN std_logic;
        rst_n : IN std_logic;
        rd : IN std_logic;
        fifo_empty : IN std_logic
    );
END ENTITY;

ARCHITECTURE Behavioral OF read_pointer IS
    SIGNAL re : std_logic;
    SIGNAL read_addr : std_logic_vector(4 DOWNTO 0);
BEGIN
    rptr <= read_addr;
    fifo_rd <= re;
    re <= NOT fifo_empty AND rd;
    PROCESS(clk, rst_n)
    BEGIN
        IF rst_n = '0' THEN
            read_addr <= (OTHERS => '0');
        ELSIF rising_edge(clk) THEN
            IF re = '1' THEN
                read_addr <= read_addr + "00001";
            END IF;
        END IF;
    END PROCESS;
END ARCHITECTURE;
LIBRARY IEEE;
USE IEEE.Std_logic_1164.ALL;
USE ieee.std_logic_arith.ALL;
USE ieee.std_logic_unsigned.ALL;
-- FPGA projects using VHDL/ VHDL fpga4student.com VHDL code for FIFO memory Write pointer
ENTITY write_pointer IS
    PORT(
        wptr : OUT std_logic_vector(4 DOWNTO 0);
        fifo_we : OUT std_logic;
        clk : IN std_logic;
        rst_n : IN std_logic;
        wr : IN std_logic;
        fifo_full : IN std_logic
    );
END ENTITY;

ARCHITECTURE Behavioral OF write_pointer IS
    SIGNAL we : std_logic;
    SIGNAL write_addr : std_logic_vector(4 DOWNTO 0);
BEGIN
    fifo_we <= we;
    we <= NOT fifo_full AND wr;
    wptr <= write_addr;
    PROCESS(clk, rst_n)
    BEGIN
        IF rst_n = '0' THEN
            write_addr <= (OTHERS => '0');
        ELSIF rising_edge(clk) THEN
            IF we = '1' THEN
                write_addr <= write_addr + "00001";
            END IF;
        END IF;
    END PROCESS;
END ARCHITECTURE;
