library ieee;
-- library containing entity to be boxed
library neorv32;
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
  BOXED:  entity neorv32.neorv32_top
    generic map(
CLOCK_FREQUENCY => 120)
    port map(
    clk_i => clk,
    -- remaining input ports are attached to internal clocks
    rstn_i => std_ulogic'('1'),
wb_dat_i => std_ulogic_vector'((others => std_logic'('1'))),
wb_ack_i => std_ulogic'('1'),
wb_err_i => std_ulogic'('1'),
gpio_i => std_ulogic_vector'((others => std_logic'('1'))),
uart_rxd_i => std_ulogic'('1'),
spi_sdi_i => std_ulogic'('1'),
mtime_irq_i => std_ulogic'('1'),
msw_irq_i => std_ulogic'('1'),
mext_irq_i => std_ulogic'('1')

    );

end architecture box_arch;
