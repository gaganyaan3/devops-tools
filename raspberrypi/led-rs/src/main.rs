use std::error::Error;
use std::thread;
use std::time::Duration;
use rppal::gpio::Gpio;
use clap::Parser;


#[derive(Parser, Debug)]
#[command(version, about, long_about = None)]
struct Args {

    #[arg(short, long)]
    status: String,

    #[arg(short, long, default_value_t = 17)]
    gpin: u8,
}


fn main() -> Result<(), Box<dyn Error>> {

    let args = Args::parse();
    
    let mut pin = Gpio::new()?.get(args.gpin)?.into_output();

    if args.status == "on" {
        pin.set_high();
        println!("Led {}! {}", args.status,args.gpin);
        thread::sleep(Duration::from_millis(10));
        Ok(())
    } else if args.status == "off" {
        pin.set_low();
        println!("Led {}! {}", args.status,args.gpin);
        Ok(())
    } else {
        println!("status should be on or off");
        Ok(())
    }

}

// cargo run -- --status off --gpin 17
// led-rs --status off --gpin 17