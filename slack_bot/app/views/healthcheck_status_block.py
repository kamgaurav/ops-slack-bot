from datetime import datetime
from typing import List

import pytz
from slack_sdk.models.blocks import (
    Block,
    ContextBlock,
    MarkdownTextObject,
    SectionBlock,
)

from slack_bot.modules.gcp.healthcheck import healthcheck_data

def format_date_time(date_time_utc):
    date_time_est = (
        datetime.fromisoformat(date_time_utc)
        .astimezone(pytz.timezone("US/Eastern"))
        .strftime("%B %d, %Y %I:%M %p %Z")
    )
    return date_time_est

def healthcheck_status_block(user_id: str) -> List[Block]:
    try:
        message: List[Block] = []
        message.append(
            SectionBlock(
                text=MarkdownTextObject(
                    text="*GCP Services Status for us-west1*"
                )
            )
        )

        data = healthcheck_data()
        services_status = data.get_healthcheck_data()
        statusses = services_status.get("statusses")

        data_exists = statusses and not statusses == []

        prefix_color = {
            "SERVICE_OUTAGE": ":red_circle:",
            "SERVICE_DISRUPTION": ":large_yellow_circle:",
        }

        if data_exists:

            for status in statusses:
                priority = prefix_color[status["Status_Impact"]]

                message.append(
                    SectionBlock(
                        text=MarkdownTextObject(
                            text=f"{priority} {status['Status_Impact']}\n"
                            f"Service Name: {status['Service_Name']}\n"
                            f"Description: {status['Description']}\n"
                            f"Begin: {format_date_time(status['Begin'])}\n"
                            f"End: {format_date_time(status['End'])}\n"                            
                        )
                    )
                )
        else:
            message.append(
                SectionBlock(
                    text=MarkdownTextObject(text="*:change: No Service Disruption or Outage found*")
                )
            )

        return message

    except Exception as e:
        raise ("Error")
    