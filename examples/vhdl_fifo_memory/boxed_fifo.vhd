library ieee;
use ieee.std_logic_1164.all;

entity box is
  port(
    clk: in std_logic;
    o: out std_logic_vector(7 downto 0)
  );
end entity box;

architecture box_arch of box is
  signal internal_clock : std_logic;
begin
  internal_clock <= not internal_clock after 5 ns;
  BOXED: entity Work.fifo_mem
    port map(
    data_out => o,
    clk => clk,
    rst_n => internal_clock,
    wr => internal_clock,
    rd => internal_clock,
    data_in  => (others => internal_clock)
    );
end architecture box_arch;
