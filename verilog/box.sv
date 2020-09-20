module box
(
 input wire clk,
);
   
   (* dont_touch  = "true" *) krnl_vadd_rtl_adder #(
.C_DATA_WIDTH(32),
.C_NUM_CHANNELS(2)
);
 boxed // at line beginning goes the name of the module
              (
               .aclk (clk), 
               // rest of input ports get mapped to internal if it is one bit wide else to '1
               areset ('1),
s_tvalid ('1),
s_tdata ('1),
m_tready ('1)
);
  
endmodule : box
