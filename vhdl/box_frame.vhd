library ieee;
-- library containing entity to be boxed
____
use ieee.std_logic_1164.all;
entity box is
  port (
    clk: in std_logic
    );
end entity box;

architecture box_arch of box is
  attribute DONT_TOUCH : string;
  attribute DONT_TOUCH of BOXED : label is "TRUE";
begin
  BOXED:  entity ____
    ____
    port map(
    ____ => clk,
    -- remaining input ports are attached to internal clocks
    ____
    );

end architecture box_arch;
