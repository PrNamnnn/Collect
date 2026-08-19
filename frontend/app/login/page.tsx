export default function Login(){
    return (
        <div className="bg-main-light w-full h-screen flex justify-center items-center gap-[5vh]">
            <div className="w-[60vh] h-fit bg-[#f8f8f8] flex flex-col justify-center items-center py-[5.5vh] rounded-[4vh] shadow-[0vh_0vh_0.18vh_0vh_#000] gap-[3.5vh]">
                <div className="flex flex-col gap-[0.5vh]">
                    <p className="font-poppins font-semibold text-[#282828] opacity-85 tracking-tight text-[1.6vh] ml-[2vh]">Enter your name</p>
                    <input type="text" className="bg-[#ececec] w-[48vh] h-[7.5vh] rounded-[2vh] px-[2vh] font-poppins font-medium text-[1.9vh]" placeholder="Enter your name"/>
                </div>
                <div className="flex flex-col gap-[0.5vh]">
                    <p className="font-poppins font-semibold text-[#282828] opacity-85 tracking-tight text-[1.6vh] ml-[2vh]">Enter your password</p>
                    <input type="password" className="bg-[#ececec] w-[48vh] h-[7.5vh] rounded-[2vh] px-[2vh] font-poppins font-medium text-[1.9vh]" placeholder="Enter your password"/>
                </div>
                <button className="w-[48vh] h-[7vh] mt-[1vh] text-[2.3vh] bg-black text-[#fafafa] font-poppins font-[550] rounded-full  transition-all duration-200 ease-in-out hover:bg-[#f8f8f8] hover:text-black hover:font-semibold hover:shadow-[0vh_0vh_0vh_0.3vh_#000] hover:border-[0.3vh]">Login</button>
            </div>
            <div className="w-[43vh] h-[40vh] bg-black rounded-[4vh] flex flex-col justify-center items-center gap-[1vh]">
                <button className="w-[80%] h-[7.5vh] mt-[1vh] text-[2.3vh] bg-[#fafafa] text-black font-poppins font-semibold rounded-full  transition-all duration-200 ease-in-out hover:bg-black hover:text-[#fafafa] hover:font-semibold hover:shadow-[0vh_0vh_0vh_0.3vh_#fafafa] hover:border-[0.3vh]">Google</button>
                <button className="w-[80%] h-[7.5vh] mt-[1vh] text-[2.3vh] bg-[#fafafa] text-black font-poppins font-semibold rounded-full  transition-all duration-200 ease-in-out hover:bg-black hover:text-[#fafafa] hover:font-semibold hover:shadow-[0vh_0vh_0vh_0.3vh_#fafafa] hover:border-[0.3vh]">Apple</button>
                <p className="font-poppins font-medium text-[#fafafa]">or</p>
                <button className="w-[80%] h-[7.5vh] bg-black text-[#fafafa] border-[0.6vh] font-poppins font-semibold rounded-full transition-all duration-200 hover:scale-[1.01]">Forgot Password</button>
                
            </div>
        </div>
    )

}