#!/usr/bin/Rscript

# Script: Vectorize1.R
# Author: Electric Emus (dongxuan.zhu22@imperial.ac.uk, f.ferreira22@imperial.ac.uk, 
#                        amy.feakes22@imperial.ac.uk, zitong.zhao22@imperial.ac.uk,
#                        xuanyin.zheng22@imperial.ac.uk)
# Description: Practical work with vectorisation
# Date: Oct 2022

M <- matrix(runif(1000000), 1000, 1000)

SumAllElements <- function(M) {
    Dimensions <- dim(M)
    Tot <- 0
    for (i in 1:Dimensions[1]) {
        for (j in 1:Dimensions[2]) {
            Tot <- Tot + M[i,j]
        }
    }
    return (Tot)
}

cat("\nIn R, the sum function using loop takes: \n")
cat(system.time(SumAllElements(M))[[3]],"\n")

cat("In R, the sum function with in-built vectorization takes: \n")
cat(system.time(sum(M))[[3]],"\n")