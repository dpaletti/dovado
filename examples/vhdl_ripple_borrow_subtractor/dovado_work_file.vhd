LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
ENTITY rbs IS
    GENERIC(
        Nbit_rbs : integer := 4
    );
    PORT(
        minN : IN std_logic_vector(Nbit_rbs - 1 DOWNTO 0);
        subN : IN std_logic_vector(Nbit_rbs - 1 DOWNTO 0);
        binN : IN std_logic;
        boutN : OUT std_logic;
        diffN : OUT std_logic_vector(Nbit_rbs - 1 DOWNTO 0)
    );
END ENTITY;

ARCHITECTURE rtl OF rbs IS
    COMPONENT fulllsubstractor IS
        PORT(
            min : IN std_logic;
            sub : IN std_logic;
            bin : IN std_logic;
            bout : OUT std_logic;
            diff : OUT std_logic
        );
    END COMPONENT;
    SIGNAL b : std_logic_vector(Nbit_rbs - 2 DOWNTO 0);
BEGIN
