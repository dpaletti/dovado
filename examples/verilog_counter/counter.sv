module counter
  #( 	parameter N = '1,
   		parameter DOWN = 0,
parameter [7:0] PARAM_ARRAY [4 : 0]   = {8'd1, 8'd0, 8'd0, 8'd2})

  ( input 							clk,
    input 							rstn,
    input 							en,
   	output 	reg [N-1:0] out);

  always @ (posedge clk) begin
    if (!rstn) begin
      out <= 0;
    end else begin
      if (en)
        if (DOWN)
          out <= out - 1;
        else
          	out <= out + 1;
      else
         out <= out;
    end
  end
endmodule

module design_top (    input clk,
                input rstn,
                input en,
                output [1:0] out);

    counter #(.N(2)) u0 (	.clk(clk),
                          .rstn(rstn),
                          .en(en));
endmodule
