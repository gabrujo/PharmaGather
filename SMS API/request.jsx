nexmo.verify.request({
  number: RECIPIENT_NUMBER,
  brand: BRAND_NAME
}, (err, result) => {
  if (err) {
    console.error(err);
  } else {
    const verifyRequestId = result.request_id;
    console.log('request_id', verifyRequestId);
  }
});