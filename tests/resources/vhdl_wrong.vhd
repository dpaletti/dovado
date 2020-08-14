-- from https://github.com/ckevar/IIR-Filter/blob/master/src/RBS.vhd

library ieee;
use ieee.std_logic_1164.all;

entity rbs is			-- entity declaration, ripple borrow subtractor RBS
  generic (Nbit_rbs : integer); 	-- generic parameter modelling the number of bits to substract
	port (
		minN : std_logic_vector(Nbit_rbs - 1 downto 0); 	-- vector minuend
		subN : in std_logic_vector(Nbit_rbs - 1 downto 0); 	-- vector subtrahend
		binN : in std_logic; 								-- borrow in
		boutN: out std_logic; 								-- borrow out
		diffN: out std_logic_vector(Nbit_rbs - 1 downto 0) 	-- result = minuend - subtrahend
	);
end entity rbs


architecture rtl of rbs is					-- architectural description (Register-Transfer Level description)
	component fulllsubstractor is 			-- calling full substractor component
		port (
			min		: in std_logic;
			sub		: in std_logic;
			bin 	: in std_logic;
			bout	: out std_logic;
			diff	: out std_logic
		);
	end component fulllsubstractor;

	signal b : std_logic_vector(Nbit_rbs - 2 downto 0); -- internal signal used to conect the borrows between full substractors

begin
											-- generating full substractor modules
	GEN : for i in 0 to Nbit_rbs generate
		FIRST: if i = 0 generate 			-- generation full substractor for the LSB bits
			FF1 : fulllsubstractor port map (minN(i), subN(i), binN, b(i), diffN(i));
		end generate FIRST;

		INTERNAL: if (i > 0) and (i < Nbit_rbs - 1) generate
			FFI: fulllsubstractor port map (minN(i), subN(i), b(i - 1), b(i), diffN(i));
		end generate INTERNAL;

		LAST: if i = Nbit_rbs - 1 generate -- generation full substractor for the MSB bits
			FFN : fulllsubstractor port map (minN(i), subN(i), b(i - 1), boutN, diffN(i));
		end generate LAST;
	end generate GEN;

end architecture rtl;
