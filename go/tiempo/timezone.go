package tiempo

import (
	"fmt"
	"strings"
	"time"
)

func ZonaHoraria() {
	local, remote := timeDiff("America/Los_Angeles")
	fmt.Println(strings.Repeat("-", 40))
	fmt.Println(local, " | ", remote)
}

func timeDiff(timezone string) (string, string) {
	current := time.Now()
	remoteZone, err := time.LoadLocation(timezone)
	if err != nil {
		fmt.Println(err)
	}
	remoteTime := current.In(remoteZone)

	fmt.Println("The current time zone is:", current.Format(time.ANSIC))
	fmt.Println("The timezone:", timezone, "time is:", remoteTime)

	return current.Format(time.ANSIC), remoteTime.Format(time.ANSIC)
}
