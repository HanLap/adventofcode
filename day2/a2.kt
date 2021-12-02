import java.io.File

fun main() =
    File("input")
        .readLines()
        .map { it.split(' ') }
        .map { (id, v) -> id to v.toInt() }
        .fold(Triple(0, 0, 0)) { (x, d, a), (id, v) ->
          when (id) {
            "forward" -> Triple(x + v, d + v * a, a)
            "up" -> Triple(x, d, a - v)
            "down" -> Triple(x, d, a + v)
            else -> error("invalid token $id")
          }
        }
        .let { (x, d) -> x * d }
        .let(::println)
