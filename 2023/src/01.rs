use std::fs::File;
use std::io::{BufRead, BufReader};

fn puzzle(part2: bool) -> Result<i32, std::io::Error> {
    let mut result = 0;

    let digits: Vec<(&str, &str)> = vec![
        ("one", "1"),
        ("two", "2"),
        ("three", "3"),
        ("four", "4"),
        ("five", "5"),
        ("six", "6"),
        ("seven", "7"),
        ("eight", "8"),
        ("nine", "9"),
    ];

    let file = File::open("01.txt")?;
    let reader = BufReader::new(file);

    for i in reader.lines() {
        let mut line = i?.to_string();

        if part2 {
            let mut first: (Option<usize>, Option<&str>) = (None, None);
            let mut last: (Option<usize>, Option<&str>) = (None, None);

            for d in &digits {
                if let Some(fi) = line.find(d.0) {
                    if first.0.map_or(true, |first_idx| fi <= first_idx) {
                        first = (Some(fi), Some(d.1));
                    }
                }

                if let Some(li) = line.rfind(d.0) {
                    if last.0.map_or(true, |last_idx| li >= last_idx) {
                        last = (Some(li), Some(d.1));
                    }
                }
            }

            if let (Some(first_idx), Some(num)) = (first.0, first.1) {
                line.insert_str(first_idx, num)
            }

            if let (Some(last_idx), Some(num)) = (last.0, last.1) {
                line.insert_str(last_idx + 1, num)
            }
        }

        let trimmed = line.trim_matches(char::is_alphabetic);

        let characters: Vec<char> = trimmed.chars().collect();

        let value = format!("{}{}", characters[0], characters[characters.len() - 1]);

        result += value.parse::<i32>().unwrap();
    }

    Ok(result)
}

fn main() {
    match puzzle(false) {
        Ok(result) => println!("Part 1: {}", result),
        Err(err) => eprintln!("Error: {}", err),
    }

    match puzzle(true) {
        Ok(result) => println!("Part 2: {}", result),
        Err(err) => eprintln!("Error: {}", err),
    }
}
