## Background 背景


## Evaluation 评估

**Mean Absolut Error (MAE)**

*logerror = log(Zestimate) - log(SalePrice)*

### Submission

Submission File
For each property (unique parcelid), you must predict a log error for each time point. You should be predicting 6 timepoints: **October 2016 (201610)**, **November 2016 (201611)**, **December 2016 (201612)**, **October 2017 (201710)**, **November 2017 (201711)**, and **December 2017 (201712)**. The file should contain a header and have the following format:

> ParcelId,201610,201611,201612,201710,201711,201712
10754147,0.1234,1.2234,-1.3012,1.4012,0.8642-3.1412
10759547,0,0,0,0,0,0
etc.

Note that the actual log errors are accurate the 4th decimal places, so you can adjust your decimal formats to limit the size of your submission file.