module box //here we have parameters
#(
  parameter integer SHADOW_C_NUM_CHANNELS = 2 
 )
(
 input wire clk,
 output wire [SHADOW_C_NUM_CHANNELS-1:0] o
);
   
   logic    internal; // replication in verilog {(MAX-MIN){data_track}}
   initial begin
      internal <= 0;
      forever #(5) internal = ~ internal;
   end

   (* dont_touch  = "true" *) krnl_vadd_rtl_adder #() boxed // at line beginning goes the name of the module
              (
               .aclk (clk), 
               .s_tready (o),
               // rest of input ports get mapped to internal if it is one bit wide else to '1
               .areset ('1),
               .s_tvalid ('1),
               .m_tready (internal));
   
endmodule : box 
