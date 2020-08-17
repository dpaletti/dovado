module box //here we have parameters
#(
 )
(
 input wire clk,
 output reg[2:0] o
);
   
   (* dont_touch  = "true" *) traffic_light #() boxed // at line beginning goes the name of the module
              (
               .clk (clk), 
               // rest of input ports get mapped to internal if it is one bit wide else to '1
               .C ('1),
               .rst_n ('1)
               );
   
endmodule : box 
