main = do
    input <- readFile "input"
    print $ start $ map read $ lines input


start :: [Int] -> Int
start (fst:snd:trd:tail) = process (fst + snd + trd) $ snd:trd:tail
start _ = 0

process :: Int -> [Int] -> Int
process last (fst:snd:trd:tail) = (if curr > last then 1 else 0) + process curr (snd:trd:tail)
    where
        curr = fst + snd + trd
process _ _ = 0