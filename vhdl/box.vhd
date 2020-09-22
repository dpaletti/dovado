LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
ENTITY box IS
    PORT(
        clk : IN std_logic
    );
END ENTITY;

ARCHITECTURE box_arch OF box IS
attribute DONT_TOUCH : string;
attribute DONT_TOUCH of BOXED : label is "TRUE";
BEGIN
    BOXED: entity work.rbs GENERIC MAP(
        Nbit_rbs => 4
    ) PORT MAP(
        binN => clk,
        minN => std_logic_vector'(OTHERS => '1'),
        subN => std_logic_vector'(OTHERS => '1')
    );
END ARCHITECTURE;
