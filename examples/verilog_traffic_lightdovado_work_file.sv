module traffic_light #(
    parameter HGRE_FRED = {'__class__': 'HdlValueInt', 'base': 2, 'bits': 2, 'val': '00'}
    ,
    // Highway green and farm red
    parameter HYEL_FRED = {'__class__': 'HdlValueInt', 'base': 2, 'bits': 2, 'val': '01'}
    ,
    // Highway yellow and farm red
    parameter HRED_FGRE = {'__class__': 'HdlValueInt', 'base': 2, 'bits': 2, 'val': '10'}
    ,
    // Highway red and farm green
    parameter HRED_FYEL = {'__class__': 'HdlValueInt', 'base': 2, 'bits': 2, 'val': '11'}

) (
    // reset active low
    output reg[2:0] light_highway,
    output reg[2:0] light_farm,
    // Highway red and farm yellow
    input wire C,
    input wire clk,
    input wire rst_n
);
    // output of lights
    // fpga4student.com FPGA projects, VHDL projects, Verilog projects
    reg[27:0] count = 0;
    reg[27:0] count_delay = 0;
    reg delay10s = 0;
    reg delay3s1 = 0;
    reg delay3s2 = 0;
    reg RED_count_en = 0;
    reg YELLOW_count_en1 = 0;
    reg YELLOW_count_en2 = 0;
    wire clk_enable;
    // clock enable signal for 1s
    reg[1:0] state;
    reg[1:0] next_state;
    // next state
    always @(posedge clk, negedge rst_n)
        if (~rst_n)
            state <= 2'b00;
        else
            state <= next_state;
    // FSM
    always @(*)
        case(state)
            HGRE_FRED: begin
                RED_count_en = 0;
                YELLOW_count_en1 = 0;
                YELLOW_count_en2 = 0;
                light_highway = 3'b001;
                light_farm = 3'b100;
                if (C)
                    next_state = HYEL_FRED;
                else
                    next_state = HGRE_FRED;
            end
            HYEL_FRED: begin
                light_highway = 3'b010;
                light_farm = 3'b100;
                RED_count_en = 0;
                YELLOW_count_en1 = 1;
                YELLOW_count_en2 = 0;
                if (delay3s1)
                    next_state = HRED_FGRE;
                else
                    next_state = HYEL_FRED;
            end
            HRED_FGRE: begin
                light_highway = 3'b100;
                light_farm = 3'b001;
                RED_count_en = 1;
                YELLOW_count_en1 = 0;
                YELLOW_count_en2 = 0;
                if (delay10s)
                    next_state = HRED_FYEL;
                else
                    next_state = HRED_FGRE;
            end
            HRED_FYEL: begin
                light_highway = 3'b100;
                light_farm = 3'b010;
                RED_count_en = 0;
                YELLOW_count_en1 = 0;
                YELLOW_count_en2 = 1;
                if (delay3s2)
                    next_state = HGRE_FRED;
                else
                    next_state = HRED_FYEL;
            end
            default:
                next_state = HGRE_FRED;
        endcase

    // fpga4student.com FPGA projects, VHDL projects, Verilog projects
    // create red and yellow delay counts
    always @(posedge clk)
        if (clk_enable == 1) begin
            if (RED_count_en || YELLOW_count_en1 || YELLOW_count_en2)
                count_delay <= count_delay + 1;
            if (count_delay == 9 && RED_count_en) begin
                delay10s = 1;
                delay3s1 = 0;
                delay3s2 = 0;
                count_delay <= 0;
            end else if (count_delay == 2 && YELLOW_count_en1) begin
                delay10s = 0;
                delay3s1 = 1;
                delay3s2 = 0;
                count_delay <= 0;
            end else if (count_delay == 2 && YELLOW_count_en2) begin
                delay10s = 0;
                delay3s1 = 0;
                delay3s2 = 1;
                count_delay <= 0;
            end else begin
                delay10s = 0;
                delay3s1 = 0;
                delay3s2 = 0;
            end
        end

    // create 1s clock enable 
    always @(posedge clk) begin
        count <= count + 1;
        //if(count == 50000000) // 50,000,000 for 50 MHz clock running on real FPGA
        if (count == 3)
            // for testbench
            count <= 0;
    end

    assign clk_enable = (count == 3) ? 1 : 0;
endmodule
