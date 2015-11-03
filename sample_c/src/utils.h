#include <assert.h>
#include <err.h>
#include <errno.h>
#include <limits.h>
#include <stdint.h>
#include <string.h>
#include <unistd.h>

__attribute__ ((__warn_unused_result__))  __attribute__ ((__nonnull__))
static inline ssize_t partial_read(uint8_t* buf, size_t len)
{
    assert(len <= SSIZE_MAX);
    ssize_t r;
    uint8_t *rbuf = buf;
    do {
        do {
            r = read(0, rbuf, len);
        } while (r == EINTR);
        if (r == -1)
            err(120, "Read error!");
        if (r == 0)
            break;
        len -= r;
        rbuf += r;
    } while (len != 0);
    return rbuf - buf;
}

__attribute__ ((__warn_unused_result__))  __attribute__ ((__nonnull__))
static inline ssize_t partial_write(const uint8_t* buf, size_t len)
{
    assert(len <= SSIZE_MAX);
    ssize_t w;
    const uint8_t *wbuf = buf;
    do {
        do {
            w = write(1, wbuf, len);
        } while (w == EINTR);
        if (w == -1)
            err(120, "Write error!");
        if (w == 0)
            break;
        len -= w;
        wbuf += w;
    } while (len != 0);
    return wbuf - buf;
}

__attribute__((__nonnull__))
static inline void in(uint8_t *buf, size_t len)
{
    if (partial_read(buf, len) != (ssize_t) len)
        errx(120, "Couldn't read all the data!");
}

__attribute__((__nonnull__))
static inline void out(const uint8_t *buf, size_t len)
{
    if (partial_write(buf, len) != (ssize_t) len)
        errx(120, "Couldn't write all the data!");
}


__attribute__((__nonnull__))
static inline void string_out(const char *str)
{
    out((const uint8_t*) str, strlen(str));
}
