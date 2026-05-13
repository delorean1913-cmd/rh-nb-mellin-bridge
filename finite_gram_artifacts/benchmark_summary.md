# NB Gram benchmark summary

Layer: **finite diagnostic** unless accompanied by exact or interval certificates.

## Closed-form Gram computation summary

The benchmark program records a closed-form Gram entry approach for

```math
G_{ab}=\int_0^\infty \{t/a\}\{t/b\}{dt\over t^2}.
```

It reports high-precision closed-form runs at 100 decimal digits for \(N=10,20,30,40,50\), and a float64 diagnostic extension through \(N=100\).

## High-precision table

| N | delta_N | delta_N^2 | sqrt(log N) delta_N | condition number, float64 diagnostic |
|---:|---:|---:|---:|---:|
| 10 | 0.15418127498512773 | 0.02377186555603957 | 0.23395884950562424 | 329.425161952888 |
| 20 | 0.12846627211463010 | 0.01650358307103019 | 0.22235178532038915 | 1352.510066383304 |
| 30 | 0.12054090788664756 | 0.01453011047413725 | 0.22230558629934938 | 3052.457786173109 |
| 40 | 0.11276168318775936 | 0.01271519719533661 | 0.21657522870560330 | 5656.759044775769 |
| 50 | 0.10894516449157147 | 0.01186904886609557 | 0.21548083955822315 | 9409.568555891985 |

## Float64 diagnostic extension

| N | delta_N | delta_N^2 | sqrt(log N) delta_N | condition number |
|---:|---:|---:|---:|---:|
| 75 | 0.10519005077660470 | 0.01106494678238468 | 0.21856984286460400 | 21176.377326059894 |
| 100 | 0.10093940014423197 | 0.01018876250147738 | 0.21661252342354784 | 37254.17945768159 |

The float64 extension is a finite diagnostic only. It should not be labeled as a certified high-precision theorem artifact until a verifier or interval certificate is included.
