#![feature(plugin)]
#[plugin] #[no_link]
extern crate regex_macros;
extern crate regex;

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
                Err(why) => panic!("syntax error: {:?}", why),
            }
        },
        Err(why) => panic!("io error: {}", why),
    }
}

#[allow(unused_must_use)]
fn main() {
    let reg_tag = regex!(r"<[a-z^<^>/]*>");
    let questions = read_questions("questions.py");
    let indices = range(1, questions.len()).rev();
    let mut q_i = questions.iter().zip(indices);
    let mut input = io::stdio::stdin();

    for ((q, a), r) in q_i {
        println!("{} questions remaining!", r);
        println!("Press any key for question...");
        input.read_line();
        println!("Question: {}", q);
        println!("Press any key for answer...");
        input.read_line();
        let pretty_a = reg_tag.replace_all(a.as_slice(), "");
        println!("Answer: {}", pretty_a);
    }

    println!("Congratulations, you are done.");
}
