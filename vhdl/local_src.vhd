LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
USE ieee.std_logic_unsigned.ALL;
USE work.GenericsPack.ALL;
USE work.OpCodePack.ALL;
ENTITY Tile IS
    GENERIC(
        AddressWidthInstr : positive := 8;
        AddressWidthData : positive := 6
        ;
        CharacterNumber : positive := 14
        ;
        OpCodeBus : positive := 10
        ;
        OpCodeWidth : positive := 6
        ;
        InternalOpBus : positive := 2
        ;
        DataWidth : positive := 8
        ;
        ClusterWidth : positive := 4
        ;
        NCluster : positive := 4
        ;
        CounterWidth : positive := 3
        ;
        BufferAddressWidth : positive := 3
        ;
        StackDataWidth : positive := 24
        ;
        ExternalBusWidthData : positive := 128
        ;
        InternalBusWidthData : positive := 56
        ;
        ExternalBusWidthInstr : positive := 32
        ;
        RamWidthInstr : positive := 38
        ;
        RamWidthData : positive := 8

    );
    PORT(
        clk : IN std_logic;
        rst : IN std_logic;
        addr_start_instr : IN std_logic_vector(AddressWidthInstr - 1 DOWNTO 0);
        first_character : IN std_logic_vector(CharacterNumber - 1 DOWNTO 0);
        ending_character : IN std_logic_vector(CharacterNumber - 1 DOWNTO 0);
        curr_character : OUT std_logic_vector(CharacterNumber - 1 DOWNTO 0);
        curr_last_match_char : OUT std_logic_vector(CharacterNumber - 1 DOWNTO 0);
        reload_bram : OUT std_logic_vector(1 DOWNTO 0);
        reload_complete : IN std_logic;
        src_en : IN std_logic;
        complete : OUT std_logic;
        found : OUT std_logic;
        where_complete : OUT std_logic_vector(2 DOWNTO 0);
        instr_address_wr : IN std_logic_vector(AddressWidthInstr - 1 DOWNTO 0);
        instr_data_in : IN std_logic_vector(ExternalBusWidthInstr - 1 DOWNTO 0);
        instr_we_data : IN std_logic;
        instr_we_opcode : IN std_logic;
        data_address_wr : IN std_logic_vector(AddressWidthData - 1 DOWNTO 0);
        data_data_in : IN std_logic_vector(ExternalBusWidthData - 1 DOWNTO 0);
        data_we : IN std_logic
    );
END ENTITY;

ARCHITECTURE Behavioral OF Tile IS
    SIGNAL ram_instr_addr_rd_1_int : std_logic_vector(AddressWidthInstr - 1 DOWNTO 0);
    SIGNAL ram_instr_out_1_int : std_logic_vector(RamWidthInstr - 1 DOWNTO 0);
    SIGNAL ram_instr_addr_rd_2_int : std_logic_vector(AddressWidthInstr - 1 DOWNTO 0);
    SIGNAL ram_instr_out_2_int : std_logic_vector(RamWidthInstr - 1 DOWNTO 0);
    SIGNAL ram_instr_out_3_int : std_logic_vector(RamWidthInstr - 1 DOWNTO 0);
    SIGNAL ram_instr_addr_rd_3_int : std_logic_vector(AddressWidthInstr - 1 DOWNTO 0);
    SIGNAL ram_data_address_rd_int : std_logic_vector(AddressWidthData - 1 DOWNTO 0);
    SIGNAL ram_data_out_int : std_logic_vector(InternalBusWidthData - 1 DOWNTO 0);
BEGIN
    RAMDATA: work.RamData GENERIC MAP(
        RamWidth => RamWidthData,
        ExternalBusWidth => ExternalBusWidthData,
        InternalBusWidth => InternalBusWidthData,
        AddressWidth => AddressWidthData
    ) PORT MAP(
        rst => rst,
        clk => clk,
        address_rd => ram_data_address_rd_int,
        address_wr => data_address_wr,
        data_in => data_data_in,
        we => data_we,
        data_out => ram_data_out_int
    );
    RAMINSTRUCTION: work.RamInstr GENERIC MAP(
        BusWidth => ExternalBusWidthInstr,
        DataWidth => DataWidth,
        OpCodeWidth => OpCodeWidth,
        ClusterWidth => ClusterWidth,
        RamWidth => RamWidthInstr,
        AddressWidth => AddressWidthInstr
    ) PORT MAP(
        rst => rst,
        clk => clk,
        address_rd_1 => ram_instr_addr_rd_1_int,
        address_rd_2 => ram_instr_addr_rd_2_int,
        address_rd_3 => ram_instr_addr_rd_3_int,
        address_wr => instr_address_wr,
        data_in => instr_data_in,
        we_data => instr_we_data,
        we_opcode => instr_we_opcode,
        data_out_1 => ram_instr_out_1_int,
        data_out_2 => ram_instr_out_2_int,
        data_out_3 => ram_instr_out_3_int
    );
    TiReXCORE: work.TirexCore GENERIC MAP(
        AddressWidthInstr => AddressWidthInstr,
        AddressWidthData => AddressWidthData,
        CharacterNumber => CharacterNumber,
        OpCodeBus => OpCodeBus,
        OpCodeWidth => OpCodeWidth,
        InternalOpBus => InternalOpBus,
        DataWidth => DataWidth,
        ClusterWidth => ClusterWidth,
        NCluster => NCluster,
        BusWidthData => InternalBusWidthData,
        CounterWidth => CounterWidth,
        BufferAddressWidth => BufferAddressWidth,
        StackDataWidth => StackDataWidth,
        RamWidthInstr => RamWidthInstr
    ) PORT MAP(
        clk => clk,
        rst => rst,
        addr_start_instr => addr_start_instr,
        first_character => first_character,
        ending_character => ending_character,
        curr_character => curr_character,
        curr_last_match_char => curr_last_match_char,
        reload_bram => reload_bram,
        reload_complete => reload_complete,
        src_en => src_en,
        complete => complete,
        found => found,
        where_complete => where_complete,
        addr_instruction_1 => ram_instr_addr_rd_1_int,
        instruction_1 => ram_instr_out_1_int,
        addr_instruction_2 => ram_instr_addr_rd_2_int,
        instruction_2 => ram_instr_out_2_int,
        addr_instruction_3 => ram_instr_addr_rd_3_int,
        instruction_3 => ram_instr_out_3_int,
        addr_data => ram_data_address_rd_int,
        data => ram_data_out_int
    );
END ARCHITECTURE;
