library ieee;
use ieee.std_logic_1164.all;
____; -- library of the entity to be boxed

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
    port map(
    ____
    );

end architecture box_arch;
