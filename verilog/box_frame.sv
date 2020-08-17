module box
(
 input wire clk,
);
   
   (* dont_touch  = "true" *) ____ #() boxed // at line beginning goes the name of the module
              (
               .____ (clk), 
               .____ (o),
               // rest of input ports get mapped to internal if it is one bit wide else to '1
               ____)  
endmodule : box
