// RLVa Integration Test Script
// This script tests the @version, @versionnew, and @versionnum commands.

integer gChannel = 1234;
integer gState = 0;

default
{
    state_entry()
    {
        llOwnerSay("TST: Starting RLVa integration test...");

        // Set up listener on the specified channel
        llListen(gChannel, "", "", "");

        // Send the first command
        llOwnerSay("@version=" + (string)gChannel);
        llOwnerSay("TST: Sent @version command.");
    }

    listen(integer channel, string name, key id, string message)
    {
        if (channel == gChannel)
        {
            if (gState == 0)
            {
                llOwnerSay("TST: Received reply to @version: " + message);

                // Validate the message format for @version
                if (llSubStringIndex(message, "RestrainedLife viewer v") == 0)
                {
                    llOwnerSay("✔️ @version output format is correct.");
                    gState = 1;
                    llOwnerSay("✔️ @version test passed.");

                    // Send the next command
                    llOwnerSay("@versionnew=" + (string)gChannel);
                    llOwnerSay("TST: Sent @versionnew command.");
                }
                else
                {
                    llOwnerSay("❌ Error: @version output format is incorrect.");
                }
            }
            else if (gState == 1)
            {
                llOwnerSay("TST: Received reply to @versionnew: " + message);

                // Validate the message format for @versionnew
                if (llSubStringIndex(message, "RestrainedLove viewer v") == 0)
                {
                    llOwnerSay("✔️ @versionnew output format is correct.");
                    gState = 2;
                    llOwnerSay("✔️ @versionnew test passed.");

                    // Send the final command
                    llOwnerSay("@versionnum=" + (string)gChannel);
                    llOwnerSay("TST: Sent @versionnum command.");
                }
                else
                {
                    llOwnerSay("❌ Error: @versionnew output format is incorrect.");
                }
            }
            else if (gState == 2)
            {
                llOwnerSay("TST: Received reply to @versionnum: " + message);

                // Validate the message format for @versionnum
                if ((string)((integer)message) == message)
                {
                    llOwnerSay("✔️ @versionnum output format is correct.");
                    llOwnerSay("✔️ @versionnum test passed.");
                    llOwnerSay("✔️ All tests passed successfully.");
                }
                else
                {
                    llOwnerSay("❌ TST: Error: @versionnum output format is incorrect.");
                }
            }
        }
    }
}
