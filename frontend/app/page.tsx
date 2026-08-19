import Link from "next/link"
export default function Home(){
  return(
    <div className="main flex w-full h-screen justify-around bg-[#E9E4D8]">
      <div className="left w-[55%]">
        <img src="/images/home_door.svg" alt="" className="h-screen"/>
      </div>
      <div className="right flex flex-col w-[45%] justify-center items-center gap-[2vh]">
        <h1 className="font-inknut font-bold text-[7vh] tracking-tighter ml-[-13vh] mb-[-2vh]">Collect.</h1>
        <p className="terms h-fit w-[40vh] font-inknut font-medium text-[2.3vh] tracking-tight leading-tight mt-0 ">
        An ultimate notes taking app
        powered with your favoured term
        “AI” ~
        </p>
        
        <div className="buttons flex flex-col gap-[2vh] pt-[5vh]">
          <Link href="/signup">
            <button className="w-[40vh] h-[8vh] bg-black text-[#fafafa] font-poppins font-[550] rounded-full  transition-all duration-200 ease-in-out hover:bg-[#E9E4D8] hover:text-black hover:font-bold hover:shadow-[0vh_0vh_0vh_0.3vh_#000] hover:border-[0.3vh]">Signup</button>
          </Link>
          <Link href="/login">
          <button className="w-[40vh] h-[8vh] bg-[#E9E4D8] text-black border-[0.3vh] shadow-[0vh_0vh_0vh_0.3vh_#000] font-poppins font-bold rounded-full transition-all duration-200 hover:scale-[1.02]">Login</button>
          </Link>
        </div>
      </div>
    </div>
  )
}