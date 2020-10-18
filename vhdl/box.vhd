LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE work.pp_types.ALL;
USE work.pp_utilities.ALL;
ENTITY box IS
    PORT(
        clk : IN std_logic
    );
END ENTITY;

ARCHITECTURE box_arch OF box IS
attribute DONT_TOUCH : string;
attribute DONT_TOUCH of BOXED : label is "TRUE";
BEGIN
    BOXED: entity work.pp_potato GENERIC MAP(
        ICACHE_LINE_SIZE => 5,
        ICACHE_NUM_LINES => 386
    ) PORT MAP(
        clk => clk,
        reset => '1',
        irq => std_logic_vector'(OTHERS => '1'),
        wb_dat_in => std_logic_vector'(OTHERS => '1'),
        wb_ack_in => '1'
    );
END ARCHITECTURE;
