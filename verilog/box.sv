module box (
    input wire clk
);
    (* dont_touch  = "true" *) traffic_light #(
        .HGRE_FRED(0),
        .HYEL_FRED(1),
        .HRED_FGRE(10),
        .HRED_FYEL(11)
    ) boxed (
        .clk(clk),
        .C(1),
        .rst_n(1)
    );

endmodule
