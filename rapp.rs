extern crate serialize;

use std::collections::HashMap;
use std::io;
use serialize::json;

fn read_questions(path: &'static str) -> HashMap<String, String> {
    let contents = io::File::open(&Path::new(path)).read_to_string();
    match contents {
        Ok(data) => {
            let proper = data.replace("\"\"\"", "\"");
            let sliced = proper.as_slice().slice_from(12);
            match json::decode(sliced) {
                Ok(res) => res,
                Err(why) => panic!("syntax error: {}", why),
            }
        },
        Err(why) => panic!("io error: {}", why),
    }
}

#[allow(unused_must_use)]
fn main() {
    let questions = read_questions("questions.py");
    let mut input = io::stdio::stdin();

    for (q, a) in questions.iter() {
        println!("Press any key for question...");
        input.read_char();
        println!("Question: {}", q);
        println!("Press any key for answer...");
        input.read_char();
        println!("Answer: {}", a);
    }
}
