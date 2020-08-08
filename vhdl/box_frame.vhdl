-- libraries read from the module to be boxed
____
entity box is
  port (
    clk: in std_logic;
-- out should have the same type of the component to be instantiated
    o: out ____;)
end box;

architecture box_arch of box is
begin
  -- Here the component to box should be instantiated
  ____
end architecture
