# Yoti Python Sandbox SDK

[![Build Status](https://github.com/getyoti/yoti-python-sdk-sandbox/workflows/Tests/badge.svg?branch=master)](https://github.com/getyoti/yoti-python-sdk-sandbox/actions)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=getyoti%3Apython-sandbox&metric=coverage)](https://sonarcloud.io/dashboard?id=getyoti%3Apython-sandbox)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=getyoti%3Apython-sandbox&metric=bugs)](https://sonarcloud.io/dashboard?id=getyoti%3Apython-sandbox)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=getyoti%3Apython-sandbox&metric=code_smells)](https://sonarcloud.io/dashboard?id=getyoti%3Apython-sandbox)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=getyoti%3Apython-sandbox&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=getyoti%3Apython-sandbox)

Welcome to the Yoti Python Sandbox SDK. This repo contains the tools you need to test your Python back-end integration.

## Requirements

### Python version
Please refer to [Github Actions](https://github.com/getyoti/yoti-python-sdk-sandbox/actions?query=workflow%3ATests) to see all compatible Python versions.

Please email [clientsupport@yoti.com](mailto:clientsupport@yoti.com) if you require a version which is not listed here.

## Installing the Sandbox

To import the Yoti Sandbox SDK inside your project, you can use your favourite dependency management system.
If you are using pip, you can use the following command to set the Yoti Sandbox SDK as a dependency:

```shell
pip install yoti-sandbox
```

## Configuration

* `CLIENT_SDK_ID` is the SDK identifier generated by Yoti Hub in the Key tab when you create your app.

* `/path/to/your-pem-file.pem` is the path to the application pem file. It can be downloaded only once from the Keys tab in your Yoti Hub.

Please do not open the pem file as this might corrupt the key and you will need to create a new application.

## Code Examples

In the examples folder there are snippets for:
- [Yoti App](/examples/profile.py)
- [Doc Scan](/examples/doc_scan.py)

## Additional Information

For more information about the Yoti Sandbox, please visit https://developers.yoti.com/yoti/sandbox-app
