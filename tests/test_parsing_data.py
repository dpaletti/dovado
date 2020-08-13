fifo_mem_entity_status_signal = """
entity status_signal is
   port(
      fifo_full, fifo_empty, fifo_threshold: out std_logic;
   fifo_overflow, fifo_underflow : out std_logic;
      wr, rd, fifo_we, fifo_rd,clk,rst_n :in std_logic;
      wptr, rptr: in  std_logic_vector(4 downto 0)
   );
end status_signal;
"""

rbs_params = """
generic (Nbit_rbs : integer);
"""
