module box (
    input wire clk
);
    (* dont_touch  = "true" *) cpl_queue_manager #(
        .OP_TABLE_SIZE(146),
        .QUEUE_INDEX_WIDTH(7),
        .PIPELINE(15)
    ) boxed (
        .clk(clk),
        .rst(1),
        .s_axis_enqueue_req_queue(1),
        .s_axis_enqueue_req_tag(1),
        .s_axis_enqueue_req_valid(1),
        .m_axis_enqueue_resp_ready(1),
        .s_axis_enqueue_commit_op_tag(1),
        .s_axis_enqueue_commit_valid(1),
        .s_axil_awaddr(1),
        .s_axil_awprot(1),
        .s_axil_awvalid(1),
        .s_axil_wdata(1),
        .s_axil_wstrb(1),
        .s_axil_wvalid(1),
        .s_axil_bready(1),
        .s_axil_araddr(1),
        .s_axil_arprot(1),
        .s_axil_arvalid(1),
        .s_axil_rready(1),
        .enable(1)
    );

endmodule
