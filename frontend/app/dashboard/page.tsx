export default function Dashboard(){
    return (
        <div className="w-full h-screen bg-[#F5F5F5] flex flex-col items-center py-[5vh] gap-[5vh]">
            <div className="nav flex w-[60%] h-[10vh] bg-[#FFFFFF] shadow-[0vh_0vh_0.15vh_0vh_#282828] rounded-[3vh] px-[5vh] justify-between items-center">
                <img src="/images/dash_logo.svg" alt="" className="w-[16vh] cursor-pointer"/>
                <div className="links flex gap-[7vh] items-center justify-center">
                    <p className="font-inknut text-[1.7vh] tracking-tighter hover:underline cursor-pointer">Pricing</p>
                    <p className="font-inknut text-[1.7vh] tracking-tighter hover:underline cursor-pointer">About</p>
                    <p className="font-inknut text-[1.7vh] tracking-tighter hover:underline cursor-pointer">Programs</p>
                    <button className="w-[15vh] h-[6vh] bg-amber-200 font-poppins text-[2vh] text-black font-semibold rounded-[2vh] tracking-tighter cursor-pointer">Go Pro</button>
                </div>
            </div>
            <div className="mid">
                <div className="butts flex gap-[2vh]">
                    <button className="flex text-[2.5vh] font-inknut font-semibold tracking-tighter justify-center w-[85vh] h-[17vh] items-center text-[#fafafa] bg-black gap-[1.5vh] rounded-[4vh_1vh_1vh_1vh] transition-all duration-200 hover:scale-[1.01]"><img src="/images/white_note.svg" alt="" className="w-[4vh]"/> New note</button>
                    <button className="flex text-[2.5vh] font-inknut font-semibold tracking-tighter justify-center w-[45vh] h-[17vh] items-center text-black bg-[#ffffff] gap-[1.5vh] rounded-[1vh_4vh_1vh_1vh] transition-all duration-200 hover:scale-[1.01] shadow-[0vh_0vh_0.15vh_0vh_#282828]"><img src="/images/black_note.svg" alt="" className="w-[4vh]"/> Or Upload</button>
                </div>
            </div>
            <div className="notes bg-[#ffffff] w-full min-h-[59vh] py-[5vh_5vh] rounded-[10vh_10vh_0vh_0vh]">
                <div className="search flex w-full justify-end px-[20vh] py-[0vh_5vh] items-center">
                    <img src="/images/search.svg" alt="" className="w-[3.5vh] mr-[-6vh] z-10 mt-[0.3vh]"/>
                    <input type="search" className="bg-[#f4f4f4] w-[48vh] h-[6vh] rounded-full px-[7vh_4vh] font-poppins font-medium text-[1.9vh] transition-all duration-300 focus:w-[50%]" placeholder="Search here"/>
                </div>
                <div className="titles flex justify-between px-[25vh] font-poppins font-[550] text-[181818] tracking-tighter text-[1.6vh]">
                    <p>Name</p>
                    <p>Last updated</p>
                </div>
                <div className="flex flex-col py-[0vh_10vh]">
                    <div className="titles flex justify-between mx-[20vh] px-[5vh] h-[7vh] items-center my-[1vh] font-poppins font-[550] text-[181818] tracking-tighter text-[2.2vh] hover:bg-[#F4F4F4] rounded-[1vh]">
                        <p>Naman Prabhakar</p>
                        <p>Today</p>
                    </div>
                    <div className="titles flex justify-between mx-[20vh] px-[5vh] h-[7vh] items-center my-[1vh] font-poppins font-[550] text-[181818] tracking-tighter text-[2.2vh] hover:bg-[#F4F4F4] rounded-[1vh]">
                        <p>Lorem, ipsum dolor.</p>
                        <p>Tommorow</p>
                    </div>
                    <div className="titles flex justify-between mx-[20vh] px-[5vh] h-[7vh] items-center my-[1vh] font-poppins font-[550] text-[181818] tracking-tighter text-[2.2vh] hover:bg-[#F4F4F4] rounded-[1vh]">
                        <p>Lorem ipsum dolor sit amet.</p>
                        <p>Today</p>
                    </div>
                    <div className="titles flex justify-between mx-[20vh] px-[5vh] h-[7vh] items-center my-[1vh] font-poppins font-[550] text-[181818] tracking-tighter text-[2.2vh] hover:bg-[#F4F4F4] rounded-[1vh]">
                        <p>Lorem, ipsum dolor.</p>
                        <p>Yesterday</p>
                    </div>
                    <div className="titles flex justify-between mx-[20vh] px-[5vh] h-[7vh] items-center my-[1vh] font-poppins font-[550] text-[181818] tracking-tighter text-[2.2vh] hover:bg-[#F4F4F4] rounded-[1vh]">
                        <p>Lorem ipsum dolor sit amet.</p>
                        <p>Today</p>
                    </div>
                    <div className="titles flex justify-between mx-[20vh] px-[5vh] h-[7vh] items-center my-[1vh] font-poppins font-[550] text-[181818] tracking-tighter text-[2.2vh] hover:bg-[#F4F4F4] rounded-[1vh]">
                        <p>Lorem, ipsum dolor.</p>
                        <p>Yesterday</p>
                    </div>
                    <div className="titles flex justify-between mx-[20vh] px-[5vh] h-[7vh] items-center my-[1vh] font-poppins font-[550] text-[181818] tracking-tighter text-[2.2vh] hover:bg-[#F4F4F4] rounded-[1vh]">
                        <p>Lorem ipsum dolor sit amet.</p>
                        <p>Today</p>
                    </div>
                    <div className="titles flex justify-between mx-[20vh] px-[5vh] h-[7vh] items-center my-[1vh] font-poppins font-[550] text-[181818] tracking-tighter text-[2.2vh] hover:bg-[#F4F4F4] rounded-[1vh]">
                        <p>Lorem, ipsum dolor.</p>
                        <p>Yesterday</p>
                    </div>
                </div>
                {/* <img src="images/down_dash.svg" alt="" className="absolute bottom-[-20vh] left-0 w-full"/> */}
            </div>
        </div>
    )

}