module box (
    input wire clk
);
    (* dont_touch  = "true" *) krnl_vadd_rtl #(
        .C_S_AXI_CONTROL_DATA_WIDTH(invalid_parameter)
    ) boxed (
        .ap_clk(clk),
        .ap_rst_n(1),
        .m_axi_gmem_AWREADY(1),
        .m_axi_gmem_WREADY(1),
        .m_axi_gmem_ARREADY(1),
        .m_axi_gmem_RVALID(1),
        .m_axi_gmem_RDATA(1),
        .m_axi_gmem_RLAST(1),
        .m_axi_gmem_RID(1),
        .m_axi_gmem_RRESP(1),
        .m_axi_gmem_BVALID(1),
        .m_axi_gmem_BRESP(1),
        .m_axi_gmem_BID(1),
        .s_axi_control_AWVALID(1),
        .s_axi_control_AWADDR(1),
        .s_axi_control_WVALID(1),
        .s_axi_control_WDATA(1),
        .s_axi_control_WSTRB(1),
        .s_axi_control_ARVALID(1),
        .s_axi_control_ARADDR(1),
        .s_axi_control_RREADY(1),
        .s_axi_control_BREADY(1)
    );

endmodule
